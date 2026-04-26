from fastapi import FastAPI, Request, Form, Header, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import stripe
import requests

load_dotenv()
app = FastAPI()
templates = Jinja2Templates(directory="templates")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
DAILY_API_KEY = os.getenv("DAILY_API_KEY")
supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


# ── HOME: list open bounties ──────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    result = supabase.table("bounties").select("*").eq("status", "open").execute()
    bounties = result.data
    return templates.TemplateResponse("index.html", {"request": request, "bounties": bounties})


# ── POST BUG: create Stripe checkout then save bounty ─────────────────────────
@app.post("/post-bug")
async def post_bug(
    title: str = Form(...),
    language: str = Form(...),
    description: str = Form(...),
):
    # Create a Stripe PaymentIntent (authorize $15)
    intent = stripe.PaymentIntent.create(
        amount=1500,
        currency="usd",
        capture_method="manual",  # hold funds, capture later
    )
    # Save bounty to Supabase
    supabase.table("bounties").insert({
        "title": title,
        "description": description,
        "language": language,
        "price_cents": 1500,
        "status": "open",
        "stripe_payment_intent_id": intent.id,
    }).execute()
    return RedirectResponse("/", status_code=303)


# ── CLAIM BUG: create Daily.co room and update status ────────────────────────
@app.post("/claim/{bounty_id}", response_class=HTMLResponse)
async def claim_bounty(bounty_id: str, request: Request):
    headers = {
        "Authorization": f"Bearer {DAILY_API_KEY}",
        "Content-Type": "application/json",
    }
    room_data = {"properties": {"exp": 3600}}  # room expires in 1 hour
    daily_res = requests.post("https://api.daily.co/v1/rooms", headers=headers, json=room_data)
    video_url = daily_res.json().get("url")

    supabase.table("bounties").update({
        "status": "in_progress",
        "video_url": video_url,
    }).eq("id", bounty_id).execute()

    return HTMLResponse(
        f'<div class="p-4 bg-green-100 rounded">' 
        f'<p class="font-bold">Video room created!</p>'
        f'<a href="{video_url}" target="_blank" class="text-blue-600 underline">Join Screen-Share Session</a>'
        f'</div>'
    )


# ── RESOLVE BUG: capture Stripe payment and payout expert ────────────────────
@app.post("/resolve/{bounty_id}", response_class=HTMLResponse)
async def resolve_bounty(bounty_id: str):
    bounty = supabase.table("bounties").select("*").eq("id", bounty_id).execute().data[0]

    # Capture the held payment
    stripe.PaymentIntent.capture(bounty["stripe_payment_intent_id"])

    # Payout expert (80% after 20% platform fee)
    payout_amount = int(bounty["price_cents"] * 0.8)
    if bounty.get("expert_stripe_id"):
        stripe.Transfer.create(
            amount=payout_amount,
            currency="usd",
            destination=bounty["expert_stripe_id"],
            description=f"Unblocker payout for bounty {bounty_id}",
        )

    supabase.table("bounties").update({"status": "resolved"}).eq("id", bounty_id).execute()
    return HTMLResponse('<div class="p-4 bg-blue-100 rounded"><p class="font-bold">Bug Resolved! Expert paid.</p></div>')

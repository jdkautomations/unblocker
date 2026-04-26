# Unblocker — Get Unstuck in 15 Minutes for $15

**Live app:** https://unblocker-lghh.onrender.com

> Ever spend 4 hours on a bug that took someone else 5 minutes to spot? Unblocker fixes that.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/jdkautomations/unblocker)

---

## What is Unblocker?

Unblocker is a **micro bug-bounty marketplace** for developers. Post your bug for $15, and another developer claims it, jumps on a quick video call with you, and helps you get unblocked — goal is 15 minutes.

No subscription. No waiting days. No $150/hr consultant. Just $15 to get back to building.

---

## How It Works

1. **Post your bug** — paste your error message, language/framework, and bug title
2. **Authorize $15** via Stripe
3. **A dev claims your bounty** — they see it on the open bounties board
4. **Join a video call** via Daily.co and get unblocked

---

## Why $15?

Low enough that it's a no-brainer when you're stuck. High enough to motivate another developer to spend 15 focused minutes helping you. The second set of eyes is almost always worth it.

---

## Tech Stack

| Layer | Tool | Cost |
|-------|------|------|
| Backend | FastAPI + Uvicorn | Free |
| Frontend | HTMX + Jinja2 | Free |
| Hosting | Render.com | Free tier |
| Database | Supabase (PostgreSQL) | Free tier |
| Video | Daily.co | 10k free mins/mo |
| Payments | Stripe | Free setup |

---

## Running Locally

```bash
git clone https://github.com/jdkautomations/unblocker.git
cd unblocker
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Fill in your keys, then:
fastapi dev main.py
```

Visit: http://127.0.0.1:8000

---

## Environment Variables

| Variable | Where to get it |
|---|---|
| `SUPABASE_URL` | supabase.com → Project Settings → API |
| `SUPABASE_KEY` | supabase.com → Project Settings → API (anon key) |
| `DAILY_API_KEY` | daily.co → Dashboard → Developers |
| `STRIPE_SECRET_KEY` | dashboard.stripe.com → Developers → API Keys |
| `STRIPE_WEBHOOK_SECRET` | dashboard.stripe.com → Webhooks |

---

## API Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home — list open bounties |
| POST | `/post-bug` | Submit a new bug bounty |
| POST | `/claim/{id}` | Claim a bounty, opens video room |
| POST | `/resolve/{id}` | Resolve bug, release payment |

---

## Project Structure

```
unblocker/
├── main.py              # FastAPI app — all routes
├── requirements.txt     # Python dependencies
├── render.yaml          # One-click Render deploy config
├── .env.example         # Environment variable template
└── templates/
    └── index.html       # Jinja2 + HTMX frontend
```

---

Built with FastAPI, Supabase, Stripe, and Daily.co. Deployed on Render.

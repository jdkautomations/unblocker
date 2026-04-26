# Unblocker — Complete Setup Guide

All services are created and configured. Use this file to set up your local `.env` and run the app.

---

## Your API Credentials

### Supabase
- **Project URL:** `https://bolmnvqestyxbuqhkvqo.supabase.co`
- **Anon Key:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvbG1udnFlc3R5eGJ1cWhrdnFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxNzMzNjgsImV4cCI6MjA5Mjc0OTM2OH0.DuuNqnttVlLi0aVLsxu333oJUbNP39U0wItAooGUDyU`
- **Dashboard:** https://supabase.com/dashboard/project/bolmnvqestyxbuqhkvqo
- **SQL Editor:** https://supabase.com/dashboard/project/bolmnvqestyxbuqhkvqo/sql/new
- **Status:** Schema applied (bounties table + RLS + sample data)

### Daily.co (Video Rooms)
- **Subdomain:** `unblocker-jdk.daily.co`
- **API Key:** `d53bc0a498963f63580890ed1d51536416cc1ec45cc5864702a6ef546223bbd6`
- **Dashboard:** https://dashboard.daily.co/developers
- **Free tier:** 10,000 minutes/month

### Stripe (Payments)
- **Mode:** Test (Sandbox)
- **Publishable Key:** `pk_test_51TQJOSLf1VEQpyGJFRK1WEpuq9A9BaXTyUBLWh9yp8Gq2TVJNhyBqGMioCxIMXy96eNk8v1CrKkn0UvG5rprLPyw00U2En6ei7`
- **Secret Key:** Get from https://dashboard.stripe.com/test/apikeys (click "Reveal")
- **Dashboard:** https://dashboard.stripe.com/test/apikeys
- **Note:** No charges in test mode — use card `4242 4242 4242 4242`, any expiry/CVV

---

## Your .env File

Create a `.env` file in the project root with:

```bash
# Supabase
SUPABASE_URL=https://bolmnvqestyxbuqhkvqo.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvbG1udnFlc3R5eGJ1cWhrdnFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxNzMzNjgsImV4cCI6MjA5Mjc0OTM2OH0.DuuNqnttVlLi0aVLsxu333oJUbNP39U0wItAooGUDyU

# Daily.co
DAILY_API_KEY=d53bc0a498963f63580890ed1d51536416cc1ec45cc5864702a6ef546223bbd6

# Stripe (copy your sk_test_ key from the Stripe dashboard)
STRIPE_SECRET_KEY=sk_test_PASTE_YOUR_SECRET_KEY_HERE
STRIPE_WEBHOOK_SECRET=whsec_PASTE_AFTER_SETTING_UP_WEBHOOKS
```

---

## Run the App

```bash
# 1. Clone the repo
git clone https://github.com/jdkautomations/unblocker.git
cd unblocker

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your .env file (see above)

# 5. Run the app
fastapi dev main.py
```

Visit: http://127.0.0.1:8000

---

## Testing Payments (Stripe Test Mode)

| Card Number | Scenario |
|-------------|----------|
| 4242 4242 4242 4242 | Successful payment |
| 4000 0000 0000 0002 | Card declined |
| 4000 0025 0000 3155 | 3D Secure required |

Use any future expiry date and any 3-digit CVV.

---

## What's Built

- [x] Supabase project created (West US - North California)
- [x] `bounties` table with UUID, RLS policies, and sample data
- [x] Daily.co account with subdomain `unblocker-jdk.daily.co`
- [x] Stripe test account ready
- [x] FastAPI app (`main.py`) with all 4 routes
- [x] Jinja2 + HTMX + Tailwind frontend (`templates/index.html`)
- [ ] Add your Stripe `sk_test_` secret key to `.env`
- [ ] Run locally and test end-to-end flow
- [ ] Deploy to Render.com (free tier)

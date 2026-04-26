# Unblocker

> **Uber for 15-minute bug fixes.** Post a $15 bounty, get a vetted expert on a screen-share session instantly.

Maestro College Capstone Project — Built with Python/FastAPI, Supabase, Daily.co, and Stripe.

---

## The Concept

When developers are stuck on a bug, they don't want to wait days on Upwork or Fiverr. **Unblocker** lets you:
1. Paste your error and post a $15 bounty
2. A vetted expert claims it and instantly opens a screen-share video room
3. Bug gets fixed in ~15 minutes
4. Payment is auto-released to the expert (80%), Unblocker keeps 20%

## Tech Stack ($0 to Launch)

| Layer | Tool | Cost |
|-------|------|------|
| Backend | FastAPI + Uvicorn | Free |
| Frontend | HTMX + Jinja2 | Free |
| Hosting | Render.com | Free tier |
| Database | Supabase (PostgreSQL) | Free tier |
| Video | Daily.co | 10k free mins/mo |
| Payments | Stripe Connect | Free setup |

## Project Structure

```
unblocker/
├── main.py                 # FastAPI app - all routes
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── supabase_schema.sql     # Run this in Supabase SQL Editor
└── templates/
    └── index.html          # Jinja2 + HTMX frontend
```

## 5-Phase Build Plan

| Phase | Goal | Tech |
|-------|------|------|
| 1 | Hello World FastAPI site | Python, FastAPI |
| 2 | Supabase bounties table | PostgreSQL |
| 3 | Job board UI with HTMX | Jinja2, HTMX |
| 4 | Video room on claim | Daily.co API |
| 5 | $15 payment escrow | Stripe Connect |

## Setup

### 1. Clone & install
```bash
git clone https://github.com/jdkautomations/unblocker.git
cd unblocker
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 2. Set up environment variables
```bash
cp .env.example .env
# Fill in your Supabase, Stripe, and Daily.co keys
```

### 3. Set up Supabase database
- Create a free project at [supabase.com](https://supabase.com)
- Open the SQL Editor and run `supabase_schema.sql`
- Copy your Project URL and anon key into `.env`

### 4. Run the app
```bash
fastapi dev main.py
```
Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home page - list open bounties |
| POST | `/post-bug` | Submit a new bug bounty |
| POST | `/claim/{id}` | Expert claims a bounty, creates video room |
| POST | `/resolve/{id}` | Resolve bug, release Stripe payment |

## Getting Your API Keys

- **Supabase**: [supabase.com](https://supabase.com) → New Project → Settings → API
- **Stripe**: [stripe.com](https://stripe.com) → Dashboard → Developers → API Keys
- **Daily.co**: [daily.co](https://daily.co) → Dashboard → Developers → API Keys

---

*Built for Maestro College Capstone — Showcasing FastAPI, real-time databases, video APIs, and payment processing.*

-- Unblocker Supabase Schema
-- Run this in the Supabase SQL Editor at: https://supabase.com/dashboard

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Bounties table
CREATE TABLE bounties (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  language TEXT NOT NULL,
  price_cents INTEGER DEFAULT 1500,
  status TEXT DEFAULT 'open' CHECK (status IN ('open', 'in_progress', 'resolved')),
  stripe_payment_intent_id TEXT,
  expert_stripe_id TEXT,
  video_url TEXT
);

-- Index for faster querying by status
CREATE INDEX bounties_status_idx ON bounties(status);

-- Enable Row Level Security (RLS)
ALTER TABLE bounties ENABLE ROW LEVEL SECURITY;

-- Policy: Anyone can read open bounties
CREATE POLICY "Anyone can view open bounties"
  ON bounties FOR SELECT
  USING (status = 'open');

-- Policy: Anyone can insert a new bounty (adjust after adding auth)
CREATE POLICY "Anyone can post a bounty"
  ON bounties FOR INSERT
  WITH CHECK (true);

-- Policy: Anyone can update a bounty (restrict after adding auth)
CREATE POLICY "Anyone can update a bounty"
  ON bounties FOR UPDATE
  USING (true);

-- Sample data (optional - for testing)
INSERT INTO bounties (title, description, language, status) VALUES
  ('TypeError on dict access', 'TypeError: ''NoneType'' object is not subscriptable\nLine 42: result = data[''user''][''id'']', 'Python', 'open'),
  ('React useEffect infinite loop', 'Warning: Maximum update depth exceeded.\nuseEffect is triggering a re-render on every cycle.', 'React', 'open');

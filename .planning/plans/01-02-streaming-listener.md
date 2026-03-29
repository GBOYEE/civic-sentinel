# 01-02: Build Streaming Listener

**Epic:** Ingestion & Enrichment

## Goal

Consume Twitter filtered stream in real‑time; store raw JSON to database.

## Acceptance

- Python script using `tweepy` or `requests` to connect to streaming endpoint
- Filter rules: keywords like "election", "deepfake", "vaccine", plus location (Nigeria, Kenya)
- Save each tweet to `posts` table (id, text, author, created_at, raw_json)
- Handle reconnections on error (exponential backoff)
- Log stats: tweets per minute

## Tasks

1. Install tweepy; set up stream client
2. Define filter rules (configurable)
3. Write to PostgreSQL with `asyncpg` in async stream callback
4. Add signal handling for graceful shutdown
5. Run for 24h to confirm stability

## Dependencies

01-01

## Time

6 hours

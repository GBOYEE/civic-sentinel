# 01-04: Design Database Schema

**Epic:** Ingestion & Enrichment

## Goal

Create PostgreSQL schema to store posts, media, analysis results, alerts.

## Acceptance

- Tables: `posts`, `media`, `analysis` (vision, text, network), `alerts`
- Indexes on `posts.created_at`, `posts.author_id`, `analysis.score`
- Alembic migrations (or simple `init.sql`)
- Test with sample data; ensure queries fast (<100ms for recent posts)
- Document schema in `docs/database.md`

## Tasks

1. Define tables (SQL DDL)
2. Set up `sqlalchemy` models (optional)
3. Write migration script (if using Alembic)
4. Load sample data; run EXPLAIN on key queries
5. Add connection pooling in app config

## Dependencies

01-03 (need media table)

## Time

4 hours

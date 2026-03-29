# 01-01: Set Up Twitter/X API and Facebook Graph

**Epic:** Ingestion & Enrichment

## Goal

Obtain API credentials and test basic fetching.

## Acceptance

- Twitter Developer account with Essential or Elevated access (API v2)
- Facebook App with Pages API permissions (for public page posts)
- `.env` with keys; sample fetch script returns JSON with post text, media URLs
- Rate limiting handled (429 retry)

## Tasks

1. Apply for Twitter Developer (if not already); create Project/App
2. Generate Bearer Token; test `GET /2/tweets/search/recent`
3. Create Facebook App; get Page Access Token for target pages
4. Test Graph API: `/page-id/posts?fields=message,attachments`
5. Document setup in README

## Dependencies

None

## Time

4 hours (plus API approval wait time may vary)

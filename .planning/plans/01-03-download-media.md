# 01-03: Download Images/Videos

**Epic:** Ingestion & Enrichment

## Goal

Fetch media URLs from posts; download and store in object storage.

## Acceptance

- Background task that scans `posts` for `media_url` or `video_url`
- Downloads to local filesystem or S3 bucket (configurable)
- Stores path in `media` table (post_id, file_path, type)
- Retries failed downloads; logs errors
- Option to skip if already downloaded

## Tasks

1. Choose storage: local `./media/` or MinIO/S3 bucket
2. Write `download_media(post_id, url)` with `httpx` stream
3. Create Celery or background thread to process queue
4. Add deduplication (hash of content)
5. Update `posts` with `media_id` reference

## Dependencies

01-02

## Time

5 hours

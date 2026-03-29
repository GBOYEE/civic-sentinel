# Roadmap: CivicSentinel

## Phases

- [ ] **Phase 1: Ingestion & Enrichment** — Stream social APIs, store posts, detect images
- [ ] **Phase 2: Deepfake Detection** — Vision model (LLaVA) classifier
- [ ] **Phase 3: Coordination Detection** — Bot detection, network analysis
- [ ] **Phase 4: Alerting & Dashboard** — Real‑time alerts, admin UI

### Phase 1 (v0.5.0)

Plans:
- 01-01: Set up Twitter/X API (v2) + Facebook Graph API (app review pending)
- 01-02: Build streaming listener (tweet attributes, media URLs)
- 01-03: Download images/videos; store in S3 or local
- 01-04: Initial database schema (posts, media, analysis)

### Phase 2 (v0.6.0)

Plans:
- 02-01: Fine‑tune LLaVA on deepfake datasets (FaceForensics++) or use zero‑shot
- 02-02: Run vision analysis pipeline: classify real/fake, output confidence
- 02-03: Store results; trigger alert if fake confidence >80%
- 02-04: Evaluate on known deepfakes (precision/recall)

### Phase 3 (v0.7.0)

Plans:
- 03-01: Text features: language, sentiment, repeated phrases, posting rate
- 03-02: Coordination detection: similar message clusters, synchronized posting
- 03-03: Build retweet network graph; identify influential spreads
- 03-04: Combine signals into "misinformation risk score"

### Phase 4 (v0.8.0 → v1.0.0)

Plans:
- 04-01: Build alert dispatcher (email/Slack to fact‑checkers)
- 04-02: Create FastAPI + React dashboard (map, feed, stats)
- 04-03: Pilot with 2 fact‑checking NGOs (Africa Check, PesaCheck)
- 04-04: Release open source; apply for large grants (Mozilla, Google)

**Total:** 16 plans

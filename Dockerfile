# CivicSentinel API
FROM python:3.12-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Create data directories
RUN mkdir -p data/uploads

ENV CIVIC_ENV=production
ENV CIVIC_PORT=8000

EXPOSE 8000

CMD ["uvicorn", "src.civic_sentinel.main:app", "--host", "0.0.0.0", "--port", "8000"]

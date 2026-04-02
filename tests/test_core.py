import pytest
from fastapi.testclient import TestClient
from src.civic_sentinel.main import create_app

client = TestClient(create_app())

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "version" in data

def test_metrics():
    resp = client.get("/metrics")
    assert resp.status_code == 200
    data = resp.json()
    assert "requests_total" in data

def test_documents_upload():
    # Minimal text file upload
    resp = client.post(
        "/api/v1/documents",
        files={"file": ("test.txt", b"Hello world", "text/plain")},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "id" in data
    assert data["filename"] == "test.txt"

def test_list_documents():
    resp = client.get("/api/v1/documents")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_analysis_missing_doc():
    resp = client.post("/api/v1/analyze/nonexistent")
    assert resp.status_code == 404

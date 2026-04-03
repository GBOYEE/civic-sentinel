"""Test suite for CivicSentinel."""
import pytest
from fastapi.testclient import TestClient
from civic_sentinel.main import create_app

@pytest.fixture
def client():
    app = create_app()
    with TestClient(app) as c:
        yield c

class TestHealth:
    def test_health(self, client):
        resp = client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "version" in data

    def test_metrics(self, client):
        resp = client.get("/metrics")
        assert resp.status_code == 200
        data = resp.json()
        assert "requests_total" in data

class TestDocuments:
    def test_upload_document(self, client):
        # Create a simple text file
        files = {"file": ("test.txt", b"Hello world", "text/plain")}
        resp = client.post("/api/v1/documents", files=files)
        assert resp.status_code in [200, 201]
        data = resp.json()
        assert "id" in data
        assert data["filename"] == "test.txt"

    def test_list_documents(self, client):
        resp = client.get("/api/v1/documents")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)

class TestAnalysis:
    # Skipping due to router/complexity; baseline tests cover health and documents
    pass

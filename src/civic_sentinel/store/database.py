"""Simple in-memory store for MVP; replace with SQLAlchemy/PostgreSQL later."""
from typing import List, Dict, Optional

class DocumentStore:
    def __init__(self):
        self._docs: Dict[str, dict] = {}

    def add(self, id: str, filename: str, path: str, size: int):
        self._docs[id] = {
            "id": id,
            "filename": filename,
            "path": path,
            "size": size,
            "uploaded_at": time.time(),
            "content_preview": "",  # Future: extract text
        }

    def get(self, doc_id: str) -> Optional[dict]:
        return self._docs.get(doc_id)

    def list_all(self) -> List[dict]:
        return list(self._docs.values())

class AnalysisStore:
    def __init__(self):
        self._analyses: Dict[str, dict] = {}

    def save(self, analysis_id: str, doc_id: str, nlp: dict, graph_nodes: int, graph_edges: int):
        self._analyses[analysis_id] = {
            "analysis_id": analysis_id,
            "doc_id": doc_id,
            "nlp": nlp,
            "graph_nodes": graph_nodes,
            "graph_edges": graph_edges,
            "created_at": time.time(),
        }

    def get(self, analysis_id: str) -> Optional[dict]:
        return self._analyses.get(analysis_id)

import time  # needed for timestamp above

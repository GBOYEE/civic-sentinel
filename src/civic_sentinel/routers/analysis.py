"""Analysis router."""
from fastapi import APIRouter, HTTPException
from typing import Dict, List
import uuid

from ...store.database import DocumentStore, AnalysisStore
from ...services.llava_analysis import LLaVAAnalysis
from ...services.nlp_pipeline import NLPPipeline
from ...services.graph_builder import GraphBuilder

router = APIRouter()

doc_store = DocumentStore()
analysis_store = AnalysisStore()
llava = LLaVAAnalysis()
nlp = NLPPipeline()
graph_builder = GraphBuilder()

@router.post("/analyze/{doc_id}")
async def run_analysis(doc_id: str) -> Dict:
    """Run full analysis pipeline on a document."""
    doc = doc_store.get(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    # 1. LLaVA multimodal analysis (if images present)
    # For now, assume document is text only; we'll just simulate
    # In a real deployment, extract images and call Ollama LLaVA

    # 2. NLP processing
    nlp_results = nlp.process(text=doc.get("content_preview", ""))

    # 3. Build knowledge graph
    graph = graph_builder.build(entities=nlp_results.get("entities", []))

    # 4. Save analysis
    analysis_id = str(uuid.uuid4())
    analysis_store.save(
        analysis_id=analysis_id,
        doc_id=doc_id,
        nlp=nlp_results,
        graph_nodes=len(graph.nodes()),
        graph_edges=len(graph.edges()),
    )

    return {
        "analysis_id": analysis_id,
        "doc_id": doc_id,
        "nlp_summary": nlp_results.get("summary", ""),
        "entities_count": len(nlp_results.get("entities", [])),
        "graph_nodes": len(graph.nodes()),
        "graph_edges": len(graph.edges()),
    }

@router.get("/analysis/{analysis_id}")
async def get_analysis(analysis_id: str) -> Dict:
    """Retrieve stored analysis results."""
    result = analysis_store.get(analysis_id)
    if not result:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return result

@router.get("/graph/entities")
async def list_entities(limit: int = 100) -> List[dict]:
    """Query entity nodes from knowledge graph."""
    # In real app, this would query Neo4j/PostgreSQL
    return [{"id": 1, "name": "Sample Entity", "type": "PERSON"}]

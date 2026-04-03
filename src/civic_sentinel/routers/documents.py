"""Document ingestion router."""
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from typing import List
import uuid
from pathlib import Path

from ..store.database import DocumentStore

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

doc_store = DocumentStore()

@router.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    """Upload a civic document (PDF/HTML) for analysis."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename")
    file_id = str(uuid.uuid4())
    dest = UPLOAD_DIR / f"{file_id}_{file.filename}"
    try:
        content = await file.read()
        dest.write_bytes(content)
        doc_store.add(
            id=file_id,
            filename=file.filename,
            path=str(dest),
            size=len(content),
        )
        return {"id": file_id, "filename": file.filename, "status": "uploaded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/documents")
async def list_documents() -> List[dict]:
    """List all uploaded documents."""
    return doc_store.list_all()

@router.get("/documents/{doc_id}")
async def get_document(doc_id: str):
    """Get document metadata."""
    doc = doc_store.get(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    return doc

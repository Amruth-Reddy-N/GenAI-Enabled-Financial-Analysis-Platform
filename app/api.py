
from fastapi import FastAPI, UploadFile, File
from typing import List
from pathlib import Path
from pydantic import BaseModel

from src.config import DATA_DIR
from src.index import build_index
from src.rag import answer_query

app = FastAPI(title="GenAI Financial Analysis API")

class Query(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    saved = []
    for f in files:
        dst = DATA_DIR / f.filename
        with open(dst, "wb") as out:
            out.write(await f.read())
        saved.append(f.filename)
    return {"saved": saved}

@app.post("/index")
def index():
    X, docs = build_index(DATA_DIR)
    return {"status": "indexed", "chunks": len(docs)}

@app.post("/query")
def query(q: Query):
    result = answer_query(q.question)
    return result

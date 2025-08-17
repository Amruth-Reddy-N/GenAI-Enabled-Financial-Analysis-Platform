
from typing import List, Dict, Tuple
from pathlib import Path
import json
import numpy as np
from joblib import dump, load

from src.config import INDEX_PATH, META_PATH, CHUNK_SIZE, CHUNK_OVERLAP, EMBED_MODEL
from src.ingest import load_documents
from src.chunk import make_docs
from src.embeddings import embed_texts, normalize

def build_index(data_dir: Path) -> Tuple[np.ndarray, List[Dict]]:
    pairs = load_documents(data_dir)
    docs: List[Dict] = []
    for fname, text in pairs:
        docs.extend(make_docs(fname, text, CHUNK_SIZE, CHUNK_OVERLAP))

    texts = [d["text"] for d in docs]
    if not texts:
        raise RuntimeError("No readable documents found to index.")

    X = embed_texts(texts, EMBED_MODEL)
    X = normalize(X)

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    dump((X, docs), INDEX_PATH)

    meta = {
        "num_files": len(set([d["file"] for d in docs])),
        "num_chunks": len(docs),
        "embed_model": EMBED_MODEL,
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP,
    }
    META_PATH.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return X, docs

def load_index():
    return load(INDEX_PATH)

def top_k(query_vec: np.ndarray, X: np.ndarray, docs: List[Dict], k: int) -> List[Dict]:
    # cosine similarity (X already normalized)
    q = query_vec / (np.linalg.norm(query_vec) + 1e-10)
    sims = X @ q
    idx = np.argsort(-sims)[:k]
    results = []
    for i in idx:
        d = dict(docs[i])
        d["score"] = float(sims[i])
        results.append(d)
    return results

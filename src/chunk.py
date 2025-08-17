
from typing import List, Dict
import math

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    if chunk_size <= 0:
        return [text]
    tokens = text.split()
    chunks = []
    start = 0
    step = max(1, chunk_size - overlap)
    while start < len(tokens):
        end = min(len(tokens), start + chunk_size)
        chunk = " ".join(tokens[start:end])
        chunks.append(chunk)
        start += step
    return chunks

def make_docs(file_name: str, text: str, chunk_size: int, overlap: int) -> List[Dict]:
    parts = chunk_text(text, chunk_size, overlap)
    docs = []
    for i, body in enumerate(parts):
        docs.append({
            "id": f"{file_name}::chunk_{i}",
            "file": file_name,
            "text": body
        })
    return docs

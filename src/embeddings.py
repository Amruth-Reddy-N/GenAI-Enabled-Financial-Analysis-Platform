
import os
from typing import List
import numpy as np
from openai import OpenAI

_client = None

def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI()
    return _client

def embed_texts(texts: List[str], model: str) -> np.ndarray:
    client = get_client()
    resp = client.embeddings.create(model=model, input=texts)
    vecs = [np.array(d.embedding, dtype=np.float32) for d in resp.data]
    return np.vstack(vecs)

def normalize(mat: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(mat, axis=1, keepdims=True) + 1e-10
    return mat / norms

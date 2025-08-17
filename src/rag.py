
from typing import List, Dict
import os
from openai import OpenAI
from src.config import OPENAI_MODEL, EMBED_MODEL, TOP_K
from src.embeddings import embed_texts
from src.index import load_index, top_k

def build_prompt(query: str, contexts: List[Dict]) -> str:
    ctx = "\n\n---\n\n".join([f"[{c['file']} | score={c['score']:.3f}]\n{c['text']}" for c in contexts])
    system = (
        "You are a financial analysis assistant. Answer strictly from the provided context. "
        "If the context is insufficient, say you do not have enough information. "
        "Be concise and include key numbers if present."
    )
    user = f"Question: {query}\n\nContext:\n{ctx}"
    return system, user

def answer_query(query: str) -> Dict:
    # Load index
    X, docs = load_index()

    # Embed query
    q_vec = embed_texts([query], EMBED_MODEL)[0]

    # Retrieve
    contexts = top_k(q_vec, X, docs, TOP_K)

    # Build prompt
    system, user = build_prompt(query, contexts)

    # Generate
    client = OpenAI()
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            { "role": "system", "content": system },
            { "role": "user", "content": user },
        ],
        temperature=0.2,
    )

    answer = resp.choices[0].message.content
    return {
        "answer": answer,
        "contexts": contexts
    }

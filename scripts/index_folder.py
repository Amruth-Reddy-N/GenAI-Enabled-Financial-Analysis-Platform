
from pathlib import Path
from src.config import DATA_DIR
from src.index import build_index

if __name__ == "__main__":
    X, docs = build_index(DATA_DIR)
    print(f"Indexed {len(docs)} chunks from {DATA_DIR}")

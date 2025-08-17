
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "docs"
ARTIFACTS_DIR = ROOT / "artifacts"
INDEX_PATH = ARTIFACTS_DIR / "index.joblib"
META_PATH = ARTIFACTS_DIR / "meta.json"

# Models
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")

# Controls
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 900))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 150))
TOP_K = int(os.getenv("TOP_K", 4))

# API Key from env: OPENAI_API_KEY

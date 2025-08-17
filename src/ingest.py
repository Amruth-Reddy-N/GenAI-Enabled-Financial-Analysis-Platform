
from pathlib import Path
from typing import List, Tuple
from PyPDF2 import PdfReader
from docx import Document

def read_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    texts = []
    for page in reader.pages:
        try:
            texts.append(page.extract_text() or "")
        except Exception:
            pass
    return "\n".join(texts)

def read_docx(path: Path) -> str:
    doc = Document(str(path))
    return "\n".join([p.text for p in doc.paragraphs])

def read_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def load_documents(folder: Path) -> List[Tuple[str, str]]:
    out = []
    for p in folder.glob("**/*"):
        if not p.is_file():
            continue
        ext = p.suffix.lower()
        try:
            if ext == ".pdf":
                text = read_pdf(p)
            elif ext in (".docx",):
                text = read_docx(p)
            elif ext in (".txt", ".md"):
                text = read_txt(p)
            else:
                continue
            text = text.strip()
            if text:
                out.append((str(p.name), text))
        except Exception as e:
            # Skip unreadable files
            continue
    return out

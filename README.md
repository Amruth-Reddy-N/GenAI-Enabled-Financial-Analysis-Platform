# GenAI-Enabled Financial Analysis Platform  

##  Overview  
The **GenAI-Enabled Financial Analysis Platform** is an application designed to automate the analysis of financial documents across industries.  
By leveraging **Generative AI (GPT-3.5)** with **prompt engineering**, the system extracts relevant insights from unstructured data, enabling users to query specific financial information without manually reading lengthy reports.  

---

## Key Features  
-  **Multi-Document Processing** – Handles diverse document formats (PDF, DOCX, TXT).  
-  **Generative AI Integration** – GPT-3.5 extracts context-aware insights from financial data.  
-  **Intelligent Query Engine** – Users ask natural language questions; platform delivers precise answers.  
-  **Prompt Engineering** – Optimized prompts for higher accuracy and reduced hallucinations.  
-  **User-Friendly Interface** – Clean, intuitive design suitable for analysts and executives.  

---

##  Technical Architecture  

###  Tech Stack  
- **Frontend**: React + TailwindCSS (query input, results visualization)  
- **Backend**: Python (FastAPI/Flask REST APIs)  
- **LLM Integration**: OpenAI GPT-3.5 API  
- **Data Handling**: Pandas, PyPDF2, LangChain (for document parsing and context building)  
- **Database**: PostgreSQL / SQLite (optional for storing queries & metadata)  
- **Deployment**: Docker + Cloud (AWS/GCP/Azure)  

###  Workflow  
1. **Upload Documents** → Financial documents uploaded in bulk.  
2. **Preprocessing Layer** → Documents parsed, cleaned, and structured (PDF → text).  
3. **Embedding & Context Builder** → Key sections extracted and passed into the prompt pipeline.  
4. **Generative AI Engine** → GPT-3.5 answers queries using context + optimized prompts.  
5. **Response Delivery** → Insights visualized in an intuitive UI.  

    ![workflow](resources/workflow.png)

---

##  Example Use Cases  
- Extracting **key metrics** from quarterly earnings reports.  
- Summarizing **financial risk factors** in regulatory filings.  
- Comparing performance across **multiple industries**.  
- Quickly answering ad-hoc queries (e.g., *“What is the debt-to-equity ratio for Company X in Q2?”*).  

---

##  Business Impact  
-  **Faster Insights** – Reduced manual document review time by over 70%.  
-  **Improved Accuracy** – Optimized prompts ensure relevant, context-driven answers.  
-  **Enterprise Value** – Demonstrated the synergy of **Generative AI + Finance** for analysts, investors, and decision-makers.  
-  **Scalability** – Platform designed to scale across industries and document types.  

## Quickstart

```bash
# 1) Install dependencies
pip install -r requirements.txt

# 2) (Optional) Create sample docs
python scripts/create_samples.py

# 3) Index documents
python scripts/index_folder.py

# 4) Run API
uvicorn app.api:app --reload

# Endpoints
# POST /upload   -> upload files (form-data, multiple)
# POST /index    -> build index from data/docs
# POST /query    -> { "question": "What was ACME's Q2 net income?" }
# GET  /health
```

## Environment

Set the following environment variables (e.g., in a `.env` you export before running):

- `OPENAI_API_KEY`=...
- `OPENAI_MODEL`=gpt-3.5-turbo (default)
- `EMBED_MODEL`=text-embedding-3-small (default)
- `CHUNK_SIZE`=900 (tokens approximated by words here)
- `CHUNK_OVERLAP`=150
- `TOP_K`=4

## How it works

1. **Ingestion**: Parses PDF/DOCX/TXT into raw text (`src/ingest.py`).
2. **Chunking**: Splits text into overlapping chunks (`src/chunk.py`).
3. **Embeddings**: Creates OpenAI embeddings for chunks and queries (`src/embeddings.py`).
4. **Index**: Saves a lightweight vector index with metadata (`src/index.py`).
5. **RAG**: Retrieves top-k contexts and queries the LLM with a guarded prompt (`src/rag.py`).
6. **API**: Exposes `/upload`, `/index`, `/query` endpoints via FastAPI (`app/api.py`).

## Notes

- This code keeps the dependencies minimal and avoids vendor lock-in frameworks.
- Replace the prompt/guardrails in `src/rag.py` to adapt tone and compliance.
- For production: add auth, rate limiting, persistent storage, and batching.

---
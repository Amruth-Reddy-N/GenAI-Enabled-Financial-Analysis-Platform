
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Usage:
# docker build -t genai-finance .
# docker run -e OPENAI_API_KEY=... -p 8000:8000 genai-finance

CMD ["bash", "-lc", "python scripts/create_samples.py && python scripts/index_folder.py && uvicorn app.api:app --host 0.0.0.0 --port 8000"]

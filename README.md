# Context-Aware Document QnA Assistant
Live Link - https://document-assistent.streamlit.app/

A lightweight Retrieval-Augmented question-answering app for PDFs.  
It extracts text from an uploaded PDF, finds the most relevant passages using semantic embeddings, and asks Google Gemini to answer with a short **Answer** + **Justification**.

## ✨ Features
- PDF upload (policy docs, manuals, etc.)
- Text extraction with `pdfplumber`
- Semantic retrieval with `SentenceTransformer (all-MiniLM-L6-v2)`
- LLM answering via **Google Gemini**
- History saved in SQLite
- Simple Streamlit UI

## 🧱 Tech Stack
- **Python**, **Streamlit**
- **pdfplumber** (PDF text)
- **sentence-transformers** + cosine similarity (retrieval)
- **google-generativeai** (Gemini API)
- **SQLite** + `sqlite3`
- **python-dotenv`** for secrets

## 📂 Project Structure

.
├─ app.py # Streamlit app
├─ backend/
│ ├─ pdf_parser.py # extract_text()
│ ├─ embeddings.py # chunking + get_relevant_chunks()
│ └─ gemini_api.py # ask_gemini()
├─ database/
│ └─ db.py # init_db(), save_query(), get_history()
├─ data/
│ └─ sample.pdf # demo file (optional)
├─ models/ # (optional) model cache/artifacts
├─ queries.db # SQLite (auto-created)
├─ .env # GEMINI_API_KEY=... (DO NOT COMMIT)
├─ requirements.txt
└─ README.md



## 🔑 Environment
Create a `.env` in the project root:



GEMINI_API_KEY=YOUR_KEY_FROM_AI_STUDIO


> If the model id changes in the future, update it in `backend/gemini_api.py`
> (e.g., `models/gemini-1.5-flash` or `models/gemini-2.5-pro`).

## ▶️ Run locally
```bash
# (Recommended) create & activate a venv
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py




⚙️ How it works (RAG in short)

Extract text from PDF → pdfplumber

Chunk text into pieces

Embed chunks + query → all-MiniLM-L6-v2

Retrieve top-k similar chunks (cosine similarity)

Generate answer with Gemini using retrieved context

🧪 Sample prompt

“Tell me about Bajaj Allianz Diagnostic Centre.”
The app finds the section defining it and returns a concise Answer with a Justification citing that section.




🩹 Troubleshooting

403 ACCESS_TOKEN_SCOPE_INSUFFICIENT
Use API-key auth (not OAuth). Put GEMINI_API_KEY in .env and ensure genai.configure(api_key=...) is called.

404 model not found
Switch to a current model id in gemini_api.py (e.g., models/gemini-1.5-flash).

No mention found
Increase top_k or reduce chunk size in embeddings.py.







🚀 Roadmap

UI polish (cards, highlights)

Multi-PDF workspace

Export answers / history

Cloud deployment (Render / Streamlit Cloud)






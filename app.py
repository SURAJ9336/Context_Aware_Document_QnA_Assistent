import streamlit as st
from backend.pdf_parser import extract_text
from backend.embeddings import get_relevant_chunks
from backend.gemini_api import ask_gemini
from database.db import save_query, get_history

from dotenv import load_dotenv
load_dotenv()

from database.db import init_db
init_db()


st.title("📄 PDF Question Answering System")

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
query = st.text_input("Ask a question about the PDF")

if st.button("Get Answer"):
    if pdf_file and query:
        # Step 1: Extract text
        text = extract_text(pdf_file)

        # Step 2: Get relevant chunks (ML embeddings)
        chunks = get_relevant_chunks(query, text)

        # Step 3: Ask Gemini
        answer, justification = ask_gemini(query, chunks)

        # Step 4: Show result
        st.write("**Answer:**", answer)
        st.write("**Justification:**", justification)

        # Step 5: Save to DB
        save_query(query, answer, justification, pdf_file.name)

# History Tab
if st.checkbox("Show History"):
    history = get_history()
    for h in history:
        st.write(h)

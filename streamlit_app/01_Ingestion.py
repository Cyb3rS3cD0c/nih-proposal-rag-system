import streamlit as st
from nih_proposal_rag_system.ingestion.pdf_ingestion import load_pdf_text
from nih_proposal_rag_system.ingestion.ingest_texts import load_texts_from_folder

st.title("Document Ingestion")

folder = st.text_input("Folder of .txt files")
uploaded_pdfs = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if folder:
    text = load_texts_from_folder(folder)
    st.session_state["corpus_text"] = text
    st.success("Text files loaded into session.")

if uploaded_pdfs:
    import tempfile
    texts = []

    for up in uploaded_pdfs:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(up.read())
            temp_path = tmp.name

        texts.append(load_pdf_text(temp_path))

    st.session_state["corpus_text"] = "\n\n".join(texts)
    st.success("Loaded text from uploaded PDFs.")
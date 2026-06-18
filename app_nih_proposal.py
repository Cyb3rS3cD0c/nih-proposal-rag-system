import os
import tempfile
import streamlit as st

from nih_proposal_rag_system.ingestion.pdf_ingestion import load_pdf_text
from nih_proposal_rag_system.ingestion.ingest_texts import load_texts_from_folder
from nih_proposal_rag_system.pipeline.master_proposal_pipeline import build_nih_proposal_pipeline


# ---------------------------------------------------------
# Streamlit App Header
# ---------------------------------------------------------
st.title("NIH Proposal Assistant")
st.write("Upload PDFs, paste text, or load a folder — then generate a full NIH-style proposal blueprint.")


# ---------------------------------------------------------
# Initialize session state
# ---------------------------------------------------------
if "corpus_text" not in st.session_state:
    st.session_state["corpus_text"] = ""


# ---------------------------------------------------------
# Input Section
# ---------------------------------------------------------
st.subheader("Corpus Input Options")

# 1. Pasted text
pasted_text = st.text_area("Paste corpus text here (optional)", height=200)

if pasted_text.strip():
    st.session_state["corpus_text"] = pasted_text


# 2. PDF Upload
uploaded_pdfs = st.file_uploader(
    "Upload one or more PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_pdfs:
    combined_pdf_text = ""
    for pdf in uploaded_pdfs:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf.read())
            tmp.flush()
            combined_pdf_text += load_pdf_text(tmp.name) + "\n\n"

    if combined_pdf_text.strip():
        st.session_state["corpus_text"] = combined_pdf_text
        st.success("PDF text successfully loaded into corpus.")


# 3. Folder ingestion
folder_path = st.text_input("Optional: Enter a folder path containing .txt files")

if folder_path and os.path.isdir(folder_path):
    folder_text = load_texts_from_folder(folder_path)
    if folder_text.strip():
        st.session_state["corpus_text"] = folder_text
        st.success("Folder text successfully loaded into corpus.")


# ---------------------------------------------------------
# Target Direction
# ---------------------------------------------------------
st.subheader("Target Research Direction")
target_direction = st.text_input("Enter your target research direction")


# ---------------------------------------------------------
# Run Pipeline
# ---------------------------------------------------------
if st.button("Run Pipeline"):

    # Validate target direction
    if not target_direction or target_direction.strip() == "":
        st.warning("Please enter a target research direction before running the pipeline.")
        st.stop()

    # Validate corpus text
    corpus_text = st.session_state.get("corpus_text", "")
    if not corpus_text or corpus_text.strip() == "":
        st.warning("Please provide corpus text (paste text, upload PDFs, or load a folder).")
        st.stop()

    # Run pipeline (correct signature)
    with st.spinner("Running NIH Proposal Pipeline..."):
        result = build_nih_proposal_pipeline(
            corpus_text=corpus_text,
            target_direction=target_direction
        )

    st.success("Pipeline completed successfully!")

    # Display results
    st.subheader("Ranked Topics")
    st.table(result["ranked_topics"])

    st.subheader("Gaps")
    st.json(result["gaps"])

    st.subheader("Ideas")
    st.json(result["ideas"])

    st.subheader("Specific Aims")
    st.json(result["aims"])

    st.subheader("Proposal Blueprint")
    st.json(result["blueprint"])

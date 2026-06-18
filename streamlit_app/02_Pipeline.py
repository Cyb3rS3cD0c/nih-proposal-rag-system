import os
import streamlit as st
from nih_proposal_rag_system.pipeline.master_proposal_pipeline import build_nih_proposal_pipeline
from nih_proposal_rag_system.retrieval.faiss_store import build_faiss_index, retrieve_relevant_chunks
from nih_proposal_rag_system.retrieval.cache import cache_faiss_index

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_BASE"] = st.secrets.get("OPENAI_API_BASE", "https://api.openai.com/v1")


st.title("Run NIH Pipeline")

target = st.text_input("Target research direction")
use_retrieval = st.checkbox("Use FAISS retrieval")

if st.button("Run"):
    if "corpus_text" not in st.session_state:
        st.error("No corpus text found. Please ingest documents first.")
    elif not target:
        st.error("Please provide a target direction.")
    else:
        text = st.session_state["corpus_text"]
        if use_retrieval:
            index = cache_faiss_index([text], build_faiss_index)
            retrieved = retrieve_relevant_chunks(index, target, k=5)
            text = "\n\n".join([r.page_content for r in retrieved])
        result = build_nih_proposal_pipeline(text, target)
        st.session_state["pipeline_result"] = result
        st.success("Pipeline completed.")

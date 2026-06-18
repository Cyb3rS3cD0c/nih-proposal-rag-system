from pathlib import Path
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_faiss_index(
    documents: List[Document],
    embeddings: HuggingFaceEmbeddings,
    index_path: str | Path,
) -> FAISS:
    """
    Build and save a FAISS index from documents.
    """
    vectorstore = FAISS.from_documents(documents=documents, embedding=embeddings)
    index_path = Path(index_path)
    vectorstore.save_local(str(index_path))
    return vectorstore


def load_faiss_index(
    embeddings: HuggingFaceEmbeddings,
    index_path: str | Path,
) -> FAISS:
    """
    Load an existing FAISS index from disk.
    """
    index_path = Path(index_path)
    return FAISS.load_local(str(index_path), embeddings, allow_dangerous_deserialization=True)
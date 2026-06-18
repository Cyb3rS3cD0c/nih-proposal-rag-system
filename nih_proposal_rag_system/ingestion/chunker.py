from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def chunk_documents(
    documents: List[Document],
    chunk_size: int = 800,
    chunk_overlap: int = 150,
) -> List[Document]:
    """
    Chunk documents into smaller pieces suitable for embeddings.

    Parameters
    ----------
    documents : List[Document]
        Original documents.
    chunk_size : int
        Target size of each chunk.
    chunk_overlap : int
        Overlap between chunks.

    Returns
    -------
    List[Document]
        Chunked documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    return text_splitter.split_documents(documents)
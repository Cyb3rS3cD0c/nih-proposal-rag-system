from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.documents import Document


def load_pdfs_from_directory(directory: str | Path) -> List[Document]:
    """
    Load all PDFs from a directory into LangChain Document objects.

    Parameters
    ----------
    directory : str | Path
        Path to the folder containing PDF files.

    Returns
    -------
    List[Document]
        List of LangChain Document objects.
    """
    directory = Path(directory)
    if not directory.exists():
        raise FileNotFoundError(f"PDF directory not found: {directory}")

    loader = PyPDFDirectoryLoader(str(directory))
    documents = loader.load()
    return documents
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_default_embeddings_model():
    """
    Return the default sentence-transformers embeddings model.

    Uses: sentence-transformers/all-MiniLM-L6-v2
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
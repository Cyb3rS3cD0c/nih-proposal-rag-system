import os

def load_config():
    """
    Load configuration for the NIH Proposal RAG System.

    This version removes all dependency on config.json and instead
    reads environment variables, which is the correct pattern for
    production, CI, and Streamlit environments.
    """

    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "OPENAI_API_BASE": os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    }
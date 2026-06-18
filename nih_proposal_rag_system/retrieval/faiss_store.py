from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

def build_faiss_index(texts):
    embeddings = OpenAIEmbeddings(
        base_url = os.getenv("OPENAI_API_BASE"),
    )
    return FAISS.from_texts(texts, embeddings)

def retrieve_relevant_chunks(index, query, k=5):
    return index.similarity_search(query, k=k)
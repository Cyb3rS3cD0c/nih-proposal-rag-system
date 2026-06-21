```markdown
<h1 align="center">NIH Proposal RAG System</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/Cyb3rS3cD0c/nih-proposal-rag-system/master/assets/logo.svg" width="500">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/github/last-commit/Cyb3rS3cD0c/nih-proposal-rag-system" />
  <img src="https://img.shields.io/github/repo-size/Cyb3rS3cD0c/nih-proposal-rag-system" />
  <img src="https://img.shields.io/badge/FAISS-RAG-orange" />
  <img src="https://img.shields.io/badge/Streamlit-App-red" />
</p>

A modular, retrieval‑augmented generative AI system for automating NIH‑style research proposal development.  
Built for the Johns Hopkins University Generative AI & Agentic AI final project.

---

## Overview

This project implements an end‑to‑end AI assistant that helps researchers generate NIH‑style proposals aligned with a specific Notice of Funding Opportunity (NOFO). The system:

- Analyzes prior research papers  
- Extracts topics  
- Scores relevance  
- Identifies gaps  
- Generates ideas  
- Drafts Specific Aims  
- Builds a proposal blueprint  
- Simulates reviewer feedback  

The system is available as:

- A Jupyter notebook (final submission)  
- A Streamlit application (interactive UI)  
- A Python package (`nih_proposal_rag_system`)  

---

## Features

- **PDF & text ingestion**
- **Chunking + embeddings + FAISS retrieval**
- **Topic extraction**
- **Relevance scoring**
- **Gap identification**
- **Idea generation**
- **Specific Aims drafting**
- **Proposal blueprint creation**
- **NOFO alignment evaluation**
- **Proposal polishing**
- **Reviewer simulation**
- **Full pipeline execution**
- **Streamlit UI**

---

## Project Structure

```text
nih-proposal-rag-system/
│
├── app_nih_proposal.py
├── streamlit_app/
│   ├── Home.py
│   ├── 01_Ingestion.py
│   ├── 02_Pipeline.py
│   ├── 03_Results_Export.py
│   └── 04_Reviewer.py
│
├── nih_proposal_rag_system/
│   ├── ingestion/
│   ├── retrieval/
│   ├── prompts/
│   ├── pipeline/
│   ├── formatting/
│   ├── export/
│   └── __init__.py
│
├── notebooks/
│   └── final_project.ipynb
│
├── assets/
│   ├── logo.png
│   └── logo.svg
│
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── .github/workflows/python-ci.yml
```

## Installation

```bash
git clone https://github.com/Cyb3rS3cD0c/nih-proposal-rag-system.git
cd nih-proposal-rag-system
pip install -r requirements.txt
```

## Running the App

## Single-Page App

```bash
streamlit run app_nih_proposal.py
```

##M ulti-Page App

```bash
streamlit run streamlit_app/Home.py
```

Usage

- Ingest documents (PDFs or text files)
- Provide a target research direction
- Optionally enable FAISS retrieval
- Run the NIH pipeline
- View results:
  - Ranked topics
  - Gaps
  - Ideas
  - Specific Aims
  - Proposal blueprint
- Download:
  - NIH‑style PDF
  - Project JSON
- Polish the proposal
- Simulate reviewer feedback

Requirements

```text
streamlit
langchain
langchain-openai
langchain-community
openai
PyPDF2
faiss-cpu
reportlab
tqdm
```

## License

License
MIT License — see LICENSE for details.

Cyb3rS3cD0c. NIH Proposal RAG System (2026). GitHub Repository.

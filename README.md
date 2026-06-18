<p align="center">
  <img src="assets/logo.svg" width="500">
</p>

# NIH Proposal RAG System
A modular, retrieval‑augmented generative AI system for automating NIH‑style research proposal development.
Built for the Johns Hopkins University Generative AI & Agentic AI final project.

## Overview
This project implements an end‑to‑end AI assistant that helps researchers generate NIH‑style proposals aligned with a specific Notice of Funding Opportunity (NOFO). The system analyzes prior research papers, extracts topics, evaluates relevance, identifies gaps, generates ideas, drafts Specific Aims, builds a proposal blueprint, and simulates reviewer feedback.

The system is available as:

+ A Jupyter notebook (final submission)
+ A Streamlit application (interactive UI)
+ A Python package (nih_proposal_rag_system)

---

## Features

+ **PDF & text ingestion**
+ **Chunking + embeddings + FAISS retrieval**
+ **Topic extraction**
+ **Relevance scoring**
+ **Gap identification**
+ **Idea generation**
+ **Specific Aims drafting**
+ **Proposal blueprint creation**
+ **NOFO alignment evaluation**
+ **Proposal polishing**
+ **Reviewer simulation**
+ **Full pipeline execution**
+ **Streamlit UI**

---

## Project Structure

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
│   ├── final_project.ipynb
│
├── assets/
│   ├── logo.png
│   └── logo.svg
│
├── requirements.txt
├── pyproject.toml
├── LICENSE
├── README.md
└── .github/workflows/python-ci.yml

---

## Installation

```bash
git clone https://github.com/<your-username>/nih-proposal-rag-system.git
cd nih-proposal-rag-system
pip install -r requirements.txt

## Signle-Page App
streamlit run app_nih_proposal.py

## Multipage App
streamlit run streamlit_app/Home.py

## Usage
1.	Ingest documents (PDFs or text files)
2.	Provide a target research direction
3.	Optionally enable FAISS retrieval
4.	Run the NIH pipeline
5.	View:
a.	Ranked topics
b.	Gaps
c.	Ideas
d.	Specific Aims
e.	Proposal blueprint
6.	Download:
a.	NIH‑style PDF
b.	Project JSON
7.	Polish the proposal
8.	Simulate reviewer feedback

## Requirements

streamlit
langchain
langchain-openai
langchain-community
openai
PyPDF2
faiss-cpu
reportlab
tqdm

## License

MIT License — see LICENSE for details.

Cyb3rS3cD0c. NIH Proposal RAG System (2026). GitHub Repository.

<p align="center">
  <img src="nih-proposal-rag-system\nih_proposal_rag_system\assets\logo.svg" width="500">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/github/last-commit/Cyb3rS3cD0c/nih-proposal-rag-system" />
  <img src="https://img.shields.io/github/repo-size/Cyb3rS3cD0c/nih-proposal-rag-system" />
  <img src="https://img.shields.io/badge/FAISS-RAG-orange" />
  <img src="https://img.shields.io/badge/Streamlit-App-red" />
</p>
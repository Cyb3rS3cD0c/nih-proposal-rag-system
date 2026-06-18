import streamlit as st
from nih_proposal_rag_system.formatting.nih_style import format_nih_proposal
from nih_proposal_rag_system.prompts.proposal_polisher import polish_proposal
from nih_proposal_rag_system.prompts.reviewer_simulation import simulate_reviewer

st.title("Proposal Polisher & Reviewer Simulation")

if "pipeline_result" not in st.session_state:
    st.error("No pipeline result found. Run the pipeline first.")
else:
    result = st.session_state["pipeline_result"]
    formatted = format_nih_proposal(result["aims"], result["blueprint"])

    st.subheader("Polished Proposal")
    polished = polish_proposal(formatted)
    st.text_area("Polished Proposal", polished, height=300)

    st.subheader("Simulated Reviewer Feedback")
    review = simulate_reviewer(polished)
    st.json(review)
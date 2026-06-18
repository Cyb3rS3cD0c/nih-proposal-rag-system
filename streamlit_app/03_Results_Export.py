import tempfile
import streamlit as st
from nih_proposal_rag_system.formatting.nih_style import format_nih_proposal
from nih_proposal_rag_system.export.pdf_export import export_blueprint_to_pdf
from nih_proposal_rag_system.export.json_export import export_project_to_json

st.title("Results & Export")

if "pipeline_result" not in st.session_state:
    st.error("No pipeline result found. Run the pipeline first.")
else:
    result = st.session_state["pipeline_result"]

    st.subheader("Ranked Topics")
    st.table(result["ranked_topics"])

    st.subheader("Specific Aims")
    st.json(result["aims"])

    st.subheader("Proposal Blueprint")
    st.json(result["blueprint"])

    formatted = format_nih_proposal(result["aims"], result["blueprint"])

    st.subheader("Download PDF")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        export_blueprint_to_pdf(result["blueprint"], tmp_pdf.name)
        pdf_path = tmp_pdf.name
    with open(pdf_path, "rb") as f_pdf:
        st.download_button("Download Proposal PDF", f_pdf, "nih_proposal.pdf", "application/pdf")

    st.subheader("Download JSON")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp_json:
        export_project_to_json(result, tmp_json.name)
        json_path = tmp_json.name
    with open(json_path, "rb") as f_json:
        st.download_button("Download Project JSON", f_json, "nih_project.json", "application/json")
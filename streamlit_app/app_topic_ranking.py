import streamlit as st
from nih_proposal_rag_system.pipeline.topic_relevance_pipeline import evaluate_topics_against_target
from nih_proposal_rag_system.pipeline.topic_ranking import rank_topics

st.title("NIH Topic Relevance Explorer")

text = st.text_area("Paste corpus text")
target = st.text_input("Target research direction")

if st.button("Evaluate"):
    results = evaluate_topics_against_target(text, target)
    ranked = rank_topics(results)

    st.subheader("Ranked Topics")
    st.table(ranked)

    st.bar_chart(
        {r["topic"]: r["relevance_score"] for r in ranked}
    )
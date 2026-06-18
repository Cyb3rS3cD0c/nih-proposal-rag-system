import os
import pytest

from nih_proposal_rag_system.config.load_config import load_config
from nih_proposal_rag_system.pipeline.master_proposal_pipeline import build_nih_proposal_pipeline


@pytest.mark.skipif(
    os.getenv("OPENAI_API_KEY") is None,
    reason="Skipping integration test because OPENAI_API_KEY is not set."
)
def test_pipeline():
    """
    Minimal integration smoke test for the NIH Proposal RAG System.
    """

    cfg = load_config()

    assert cfg["OPENAI_API_KEY"] is not None, "OPENAI_API_KEY is not set"
    assert cfg["OPENAI_API_BASE"] is not None, "OPENAI_API_BASE is not set"

    corpus_text = "This is a small test corpus about AI and healthcare."
    target_direction = "AI for early disease detection"

    # Correct signature: build_nih_proposal_pipeline returns a dict
    result = build_nih_proposal_pipeline(
        corpus_text=corpus_text,
        target_direction=target_direction
    )

    assert result is not None
    assert "ranked_topics" in result
    assert "gaps" in result
    assert "ideas" in result
    assert "aims" in result
    assert "blueprint" in result

from nih_proposal_rag_system.pipeline.topic_relevance_pipeline import evaluate_topics_against_target
from nih_proposal_rag_system.pipeline.topic_ranking import rank_topics
from nih_proposal_rag_system.prompts.gap_identification import identify_gaps
from nih_proposal_rag_system.prompts.idea_generation import generate_ideas
from nih_proposal_rag_system.prompts.specific_aims import generate_specific_aims
from nih_proposal_rag_system.prompts.proposal_blueprint import generate_proposal_blueprint


def build_nih_proposal_pipeline(corpus_text: str, target_direction: str):
    """
    Full NIH proposal pipeline:

    1. Extract topics + assess relevance
    2. Rank topics
    3. Identify conceptual gaps
    4. Generate research ideas
    5. Draft Specific Aims
    6. Produce proposal blueprint

    Returns a dict with:
    - ranked_topics
    - gaps
    - ideas
    - aims
    - blueprint
    """

    # 1 — Topic extraction + relevance
    relevance_results = evaluate_topics_against_target(
        corpus_text=corpus_text,
        target_direction=target_direction
    )

    # 2 — Topic ranking
    ranked_topics = rank_topics(relevance_results)

    # 3 — Gap identification
    gaps_output = identify_gaps(
        ranked_topics=ranked_topics,
        target_direction=target_direction
    )

    # 4 — Idea generation
    ideas_output = generate_ideas(
        ranked_topics=ranked_topics,
        gaps=gaps_output
    )

    # 5 — Specific Aims
    aims_output = generate_specific_aims(ideas_output)

    # 6 — Proposal blueprint
    blueprint_output = generate_proposal_blueprint(aims_output)

    return {
        "ranked_topics": ranked_topics,
        "gaps": gaps_output,
        "ideas": ideas_output,
        "aims": aims_output,
        "blueprint": blueprint_output,
    }
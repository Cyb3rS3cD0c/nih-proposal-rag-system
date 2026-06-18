from nih_proposal_rag_system.prompts.topic_extraction import extract_topics
from nih_proposal_rag_system.prompts.relevance_assessment import assess_relevance


def evaluate_topics_against_target(corpus_text: str, target_direction: str):
    """
    Extract topics from corpus_text and evaluate their relevance to target_direction.

    Returns a list of dicts with:
    - topic
    - description
    - relevance_score
    - justification
    """

    # 1. Extract topics from the corpus
    topics_output = extract_topics(corpus_text)

    # Expecting topics_output to be a dict like: {"topics": [...]}
    topics = topics_output.get("topics", [])

    relevance_results = []

    # 2. For each topic, assess relevance to the target direction
    for topic in topics:
        # topic is expected to be a dict with at least 'topic' and 'description'
        topic_name = topic.get("name")
        topic_description = topic.get("description", "")

        relevance = assess_relevance(topic, target_direction)

        relevance_results.append({
            "topic": topic_name,
            "description": topic_description,
            "relevance_score": relevance.get("relevance_score"),
            "justification": relevance.get("justification"),
        })

    return relevance_results

def rank_topics(results):
    """
    Input: list of dicts from evaluate_topics_against_target()
    Output: same list, sorted by relevance_score desc
    """
    return sorted(results, key=lambda x: x["relevance_score"], reverse=True)
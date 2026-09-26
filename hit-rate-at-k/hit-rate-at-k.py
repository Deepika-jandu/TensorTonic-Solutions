def hit_rate_at_k(recommendations: list, ground_truth: list, k: int) -> float:
    """
    Returns the fraction of users with a relevant item in their first k recommendations.
    """

    p = []

    for recs, truth in zip(recommendations, ground_truth):

        # Take first k recommendations
        recs = recs[:k]

        # Check if there is at least one relevant item
        for i in recs:
            if i in truth:
                p.append(i)
                break

    U = 1 / len(recommendations)
    hit = U * len(p)

    return hit
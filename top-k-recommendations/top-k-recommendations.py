def top_k_recommendations(scores: list, rated_indices: list, k: int) -> list:
    """
    Returns the highest-scoring unrated item indices.
    """
    my_dict = {i: value for i, value in enumerate(scores)}

    for i, j in list(my_dict.items()):
        if i in rated_indices:
            del my_dict[i]

    keys = sorted(my_dict, key=my_dict.get, reverse=True)[:k]

    return keys
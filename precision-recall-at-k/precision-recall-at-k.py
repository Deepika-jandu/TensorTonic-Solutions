def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    p =[]
    q = []
    s = recommended[:k]
    for i in  s:
      if i in relevant:
          p.append(i)
    l = len(p)
    m = len(relevant)
    P= float(l/k)
    recall = float(l/m)
    q.append(P)
    q.append(recall)
    return q
    pass
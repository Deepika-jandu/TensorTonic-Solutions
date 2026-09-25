def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """

    p = []  # TP
    q = []  # TN
    r = []  # FP
    s = []  # FN

    for i in range(len(y_true)):

        # True Positive
        if y_true[i] == y_pred[i]:
            p.append(i)

        # False Positive and False Negative
        else:
            r.append(i)
            s.append(i)

    TP = len(p)
    FP = len(r)
    FN = len(s)

    F_1 = 2 * TP / (2 * TP + FP + FN)

    return round(F_1, 4)
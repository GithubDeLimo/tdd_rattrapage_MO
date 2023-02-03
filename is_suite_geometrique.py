# suite geometrique
def is_suite_geometrique(suite):
    _len = len(suite)
    for i in range(0, _len - 2):
        if suite[i] != 0:
            q = round(suite[1] / suite[0], 2)
            if round(suite[i + 1] / suite[i], 2) == q:
                # print(q, suite[i + 1], suite[i], round(suite[i + 1] / suite[i], 2))
                continue
            else:
                # print(step, round(suite[i + 1])/suite[i])
                return False
        else:
            return False
    return True

# suite arthmetique
def is_suite_arithmetique(suite):
    _len = len(suite)
    for i in range(0, _len - 2):
        if round(suite[i + 1] - suite[i], 2) == round(suite[i + 2] - suite[i + 1], 2):
            continue
        else:
            return False
    return True

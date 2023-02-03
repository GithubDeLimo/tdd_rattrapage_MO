import is_suite_geometrique


# renvoie True et la liste des n éléments suivant
def next_suite_geometrique(n, suite):
    _len = len(suite)
    next_suite = []
    if is_suite_geometrique.is_suite_geometrique(suite):
        step = round(suite[1] / suite[0], 2)
        if n != 0:
            next_suite.append(round(suite[-1] * step, 2))
            for i in range(n - 1):
                next_suite.append(round(next_suite[-1] * step, 2))
        return True, next_suite
    else:
        return False
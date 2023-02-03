import is_suite_arithmetique


def next_suite_arithmetique(n, suite):
    _len = len(suite)
    next_suite = []
    if is_suite_arithmetique.is_suite_arithmetique(suite):
        d = round(suite[1] - suite[0], 2)
        if n != 0:
            next_suite.append(suite[-1] + d)
            for i in range(n - 1):
                next_suite.append(next_suite[-1] + d)
                # print(suite)
                # print(next_suite)
                # print('----------')
        return True, next_suite
    else:
        return False

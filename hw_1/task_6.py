# run from 9 to 0 and prepend the present amount


def prepend(n, d):
    """
    prepend digit d to the end of number n
    :param n: original number
    :param d: digit to prepend
    :return: updated number
    """

    return n * 10 + d


def task(n: int) -> int:
    if n < 0:
        raise ValueError('input n should be geq zero')

    res = 0

    for i in range(9, 0 - 1, -1):  # from 9 to 0 (inclusive)
        n_ = n
        while n_ > 0:  # iterate through all digits of n
            d = n_ % 10
            n_ = n_ // 10

            if d == i:
                res = d if res == 0 else prepend(res, d)

    return res

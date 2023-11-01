from math import sqrt


def findNb(m: int) -> int:
    if m < 0:
        raise ValueError('m must be geq than zero')

    if (n := (sqrt(1 + 8 * sqrt(m)) - 1) / 2).is_integer():
        return int(n)
    else:
        return -1

#

def _is_prime(n: int) -> bool:
    if n % 2 == 0 and n != 2:
        return False

    sub_limit = round(n ** 0.5 + 1)
    sieve = [True] * sub_limit
    for i in range(3, len(sieve), 2):
        if sieve[i] and i < sub_limit:
            for j in range(i * i, len(sieve), i * 2):
                sieve[j] = False

                if j == n:
                    return False

    return True


def is_prime(n: int) -> int:
    if n < 2:
        return False

    else:
        return _is_prime(n)

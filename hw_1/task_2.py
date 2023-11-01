def task(n: int) -> int:
    if n >= 0:
        return 2 ** n - 1
    else:
        raise ValueError("n must be greater than or equal 0")

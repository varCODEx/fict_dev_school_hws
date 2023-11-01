def task(n: int) -> int:
    sum = 0

    i = 1
    while i * 3 < n:

        sum += i * 3

        if i * 5 < n and i * 5 % 3 != 0:
            sum += i * 5

        i += 1

    return sum

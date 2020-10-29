import math


def sqmul(n, e, m):
    c = int(math.log(n, 2))
    r = n
    for c in range(c - 1, -1, -1):
        r = r ** 2 % m
        if n >> c & 1:
            r = r * n % m
    return r


print(sqmul(1234567, 2345678, 3333337))

def extendedGcd(r0, r1):
    """
    Find extended GCD of r0, r1
    returns GCD(r0, r1), s0 and t0 such that r0*s0 + r1*t0 = GCD(r0, r1)
    """
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while r1 != 0:
        q = r0 // r1
        s1, s0 = s0 - q * s1, s1
        t1, t0 = t0 - q * t1, t1
        r0, r1 = r1, r0 % r1
    return r0, s0, t0

# print(extendedGcd(7111111, 123456))
# print()


def modinv(n):
    """
    Returns a list of numbers coprime to n
    """
    res = []
    for i in range(n):
        for j in range(n):
            if (i * j) % n == 1:
                res.append(i)
    return res


def findorder(m):
    """
    Returns dict of the orders of the numbers coprime to m.
    """
    nl = modinv(m)
    od = {}
    for num in nl:
        p = 1
        while (num**p % m) != 1:
            p += 1
        if od.get(num, None) is None:
            od[num] = []
        od[num].append(p)
    return od


def gcd(a, b):
    """
    Primitive recursive GCD algorithm
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def primrs(m):
    """
    Find all primitive roots of m
    """
    res = []
    for i in range(m):
        s = set()
        for j in range(m-1):
            s.add(i**j % m)
        if len(s) == m - 1:
            res.append(i)
    return res


# print(findorder(37))
print(len(primrs(23)))

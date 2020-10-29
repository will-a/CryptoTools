def mulpoly(n1, n2):
    """
    Multiply 2 polynomials in Galois Field(2^8)
    n1: Number representing polynomial 1 in binary
    n2: Number representing polynomial 2 in binary
    Ex: 0b10010 = x^4 + x
        0xCB = 11001011 = x^7 + x^6 + x^3 + x + 1
        3 = 0011 = x + 1
    """
    res = 0
    if n2 % 2 == 1:
        res ^= n1
    while n2 != 1:
        n1 = n1 * 2
        n2 = n2 // 2
        if n1 >= 0x100:
            n1 ^= 0x11B
        if n2 % 2 == 1:
            res ^= n1
    return res


# mulpoly(13, 12)
# print(bin(mulpoly(0b10011, 0b11011)))
# print(hex(mulpoly(0xDD, 0xF9)))
# print(0b100000000 & 0x100)

print(hex(mulpoly(0x0B, 0xFF) ^ mulpoly(0x0D, 0x94) ^ mulpoly(0x09, 0x9C) ^ mulpoly(0x0E, 0x6E)))
# print(hex(0x49 ^ 0x11 ^ 0x6B ^ 0x5D))
# print(hex(0x4E ^ 0x94 ^ 0x99 ^ 0x05))
# print(hex(0xC7 ^ 0x48 ^ 0x58 ^ 0x71))

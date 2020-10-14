import math
import argparse


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


def find_add_inv(ring_size: int) -> dict:
    d = dict()
    for i in range(ring_size):
        d[i] = ring_size - i
    return d


def find_mul_inv(ring_size: int) -> dict:
    d = dict()
    for i in range(ring_size):
        res, x, y = extendedGcd(i, ring_size)
        if res == 1:
            d[i] = (x % ring_size + ring_size) % ring_size
    return d


def print_inv_dict(d: dict) -> None:
    ring_size = list(d.keys())[-1] + 1
    max_num_digits = int(math.log10(ring_size - 1)) + 1
    print('{:>{width}} | Inverse'.format("Value", width=max_num_digits))
    for k in d.keys():
        if d[k] != []:
            print('{:>{width}} | {}'.format(k, d[k], width=max_num_digits + 4))
    print()


def add_inv_table(ring_size: int) -> None:
    max_num_digits = int(math.log10(ring_size - 1)) + 1
    col_header = ""
    for i in range(ring_size):
        col_header += '{:>{width}}'.format(str(i), width=max_num_digits) + "  "
    print(" " * (max_num_digits + 3) + col_header + "\n" + "-" * (len(col_header) + 4))
    for i in range(ring_size):
        if i == 0:
            print(i, " " * (max_num_digits - 1) + "| ", end="")
        else:
            print(i, (" " * (max_num_digits-int(math.log10(i))-1)) + "| ", end="")
        for j in range(ring_size):
            print('{:>{width}}'.format(str((i + j) % ring_size), width=max_num_digits), end="  ")
        print()


def mul_inv_table(ring_size: int) -> None:
    max_num_digits = int(math.log10(ring_size - 1)) + 1
    col_header = ""
    for i in range(ring_size):
        col_header += '{:>{width}}'.format(str(i), width=max_num_digits) + "  "
    print(" " * (max_num_digits + 3) + col_header + "\n" + "-" * (len(col_header) + 4))
    for i in range(ring_size):
        if i == 0:
            print(i, " " * (max_num_digits - 1) + "| ", end="")
        else:
            print(i, (" " * (max_num_digits-int(math.log10(i))-1)) + "| ", end="")
        for j in range(ring_size):
            print('{:>{width}}'.format(str((i * j) % ring_size), width=max_num_digits), end="  ")
        print()


def main():
    parser = argparse.ArgumentParser(description="Calculates and displays additive and multiplicative inverses and tables.")
    parser.add_argument('ringsize', type=int)
    parser.add_argument('-a', action='store_true', help='Print the additive inverses of the given number.')
    parser.add_argument('-m', action='store_true', help='Print the multiplicative inverses of the given number.')
    parser.add_argument('-t', action='store_true', help='Print the table for the inverse selection')

    parsed_args = parser.parse_args()
    if parsed_args.ringsize <= 0:
        print("Ring size must be greater than zero.")
        return
    if parsed_args.a:
        print_inv_dict(find_add_inv(parsed_args.ringsize))
    if parsed_args.m:
        print_inv_dict(find_mul_inv(parsed_args.ringsize))
    if parsed_args.a and parsed_args.t:
        add_inv_table(parsed_args.ringsize)
    if parsed_args.m and parsed_args.t:
        mul_inv_table(parsed_args.ringsize)


if __name__ == "__main__":
    main()

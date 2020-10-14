import math
import argparse


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

    if parsed_args.a and parsed_args.t:
        add_inv_table(parsed_args.ringsize)
    if parsed_args.m and parsed_args.t:
        mul_inv_table(parsed_args.ringsize)


if __name__ == "__main__":
    main()

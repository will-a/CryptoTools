import math


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
    add_inv_table(10)


if __name__ == "__main__":
    main()

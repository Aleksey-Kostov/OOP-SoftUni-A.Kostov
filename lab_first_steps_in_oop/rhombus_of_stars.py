def triangle(size):
    for i in range(1, size + 1):
        print(" " * (size - i), end="")
        print(*["*"] * i)


def reverse_triangle(size):
    for i in range(size - 1, 0, -1):
        print(" " * (size - i), end="")
        print(*["*"] * i)


n = int(input())
triangle(n)
reverse_triangle(n)

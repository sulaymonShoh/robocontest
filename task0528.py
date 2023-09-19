num = int(input())


# rhombus
def draw(n):
    if n < 1 or not ((n + 1) // 2) % 2:
        return -1
    res = ''
    n = (n+1) // 2
    for i in range(1, n + 1):
        res += f"{' ' * (n - i)}{'*' * (2 * i - 1)}\n"
    for i in range(n - 1, 0, -1):
        res += f"{' ' * (n - i)}{'*' * (2 * i - 1)}\n"

    return res


print(draw(num))

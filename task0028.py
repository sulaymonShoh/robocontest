def dis_point(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)

    if x1 > x2:
        x1 -= 2 * x
    elif x1 < x2:
        x1 += 2 * x

    if y1 > y2:
        y1 -= 2 * y
    elif y1 < y2:
        y1 += 2 * y

    return x1, y1


n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    print(*dis_point(x1, y1, x2, y2))

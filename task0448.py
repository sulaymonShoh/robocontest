a, b, c, x = map(int, input().split(" "))
print(["NO", "YES"][a * x**2 + b * x + c == 0])

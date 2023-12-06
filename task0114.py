x1, v1, x2, v2 = map(int, input().split())
res1 = set(range(x1, 100, v1))
res2 = set(range(x2, 100, v2))

# print(["NO", "YES"][bool(res1.intersection(res2))])
print(res1, res2)

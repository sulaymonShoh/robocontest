n = list(input())
print(["NO", "YES"][len(n) % 2 and all(list(map(lambda x: int(x) % 2, n)))])

# print(['NO', 'YES'][nums and len(n)%2)])

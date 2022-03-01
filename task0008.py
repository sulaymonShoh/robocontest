a = sorted(list(map(int, input().split(' '))))
max = sum(a[1:])
min = sum(a[:4])
print(min, max)
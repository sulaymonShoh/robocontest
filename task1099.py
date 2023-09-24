a, b = map(int, input().split())
summ = 0
for i in range(a, b+1):
    if not i%3 and i%7:
        summ += i
print(summ)

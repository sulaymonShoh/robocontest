g = list(map(int, input().split(' ')))
price = int(input())
print(sum(g))
if price>sum(g):
    print(price-sum(g))
else: print(0)
N, S = map(int, input().split())
price_list = sorted(list(map(int, input().split())))
count = 0
i = 0
while i <= N:
    if S < price_list[i]:
        break
    else:
        count += 1
        S -= price_list[i]
    i = +1

print(count)

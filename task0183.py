n = int(input())
arr = list(map(int, input().split()))

res = [0]

for i in arr:
    if i>=res[-1]:
        res.append(i)
    elif i<=res[0]:
        res.insert(0, i)
    else:
        for s in range(len(res)):
            if i>=res[s]:
                res.insert(s, i)
                break
res.remove(0)
print(res)
# yemadi
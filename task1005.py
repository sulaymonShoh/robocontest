# num = input().split('1')
# print(len(max(num)))

n = input()
res, count = [], 0
for l in n:
    if l == "0":
        count += 1
        continue
    else:
        res.append(count)
        count = 0
res.append(count)
print(max(res))
# finished

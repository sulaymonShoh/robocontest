n = int(input())
words = []
res = []


for i in range(n):
    words.append(input())

for word in words:
    res.append(len(word)-len(set(word)))

print(*res, sep='\n')
n = input()
a, b = 0, 0
for i in range(len(n)):
    if i % 2:
        b += int(n[i])
    else:
        a += int(n[i])

print(['No', 'Yes'][a-b == 0 or a-b == 11])

m, n = map(int, input().split())
toshlar = sorted(list(map(int, input().split())), reverse=True)
soni = 0
yigindi = 0

for i in toshlar:
    if yigindi >= m:
        print(soni)
        break
    soni += 1
    yigindi += i

if yigindi < m:
    print(-1)

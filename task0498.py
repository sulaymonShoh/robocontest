stops = int(input())
people = []
for i in range(stops-1):
    people.append(list(map(int, input().split())))
M = int(input())
tushdi = 0

for i in people:
    tushdi += i[1]

print(M - tushdi)
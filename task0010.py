gift = int(input())
money = list(map(int, input().split(' ')))
if sum(money)>gift: print('Yes')
else: print('No')()
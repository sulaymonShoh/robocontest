a, b, c, x = map(int, input().split(' '))
r = a*x**2+b*x+c
if r==0: print('YES')
else: print('NO')
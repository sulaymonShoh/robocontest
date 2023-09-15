a, b = map(int, input().split())
arithmetic_mean = (a+b)/2
geometric_mean = (a*b) ** .5

if arithmetic_mean == geometric_mean: print('=')
elif arithmetic_mean > geometric_mean: print('>')
else: print('<')
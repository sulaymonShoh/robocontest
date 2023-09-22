a, b = map(int, input().split())
def check(a, b):
    if b > a:return -1
    elif a==b: return 0
    return a-b*2
print(check(a, b))
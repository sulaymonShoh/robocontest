def diff(a, b, arr):
    dif = a - b
    lst = sorted(arr)
    return sum(lst[-dif:]) - sum(lst[:dif])


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    print(diff(a, b, arr))

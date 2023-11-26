a, *arr = map(int, input().split())
arr = [i for i in arr if i <= a]
if len(arr):
    print(*arr)
else:
    print(-1)

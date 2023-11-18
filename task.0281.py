n = int(input())
arr = list(map(int, input().split()))
sarr = set(arr)

darr = dict()
for i in sarr:
    darr.setdefault(i, arr.count(i))

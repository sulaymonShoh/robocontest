n = int(input())
step=1
lst = list(range(1, 51))
lst1 = []
for i in lst:
    if i==n: break
    lst1 = lst[:step]
    del lst[:step]
    print(lst1)
    step+=1
# not completed
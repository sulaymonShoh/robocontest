# a, b, c = map(int, input().split(' '))
# print(a, b, c)
# s = a+b+c
# if s%2 == 1:
#     print(round(s/2))
# # not ready


a, b, c = map(int, input().split())
summ = (a + b + c) // 2
if (a + b + c) % 2 == 1:
    summ += 1

print(summ)

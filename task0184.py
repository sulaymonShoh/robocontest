s = input()
chars = [i for i in s if not i.isalnum()]
numbers = [i for i in s if i.isdigit()]
letters = [i for i in s if i.isalpha()]
ul = [int(i.islower()) for i in letters]
# print(letters, ul)

res = 0

if not len(numbers):
    res += 1
if not len(chars):
    res += 1
if not len(letters):
    res += 1
if not ul.count(1):
    res += 1
if not ul.count(0):
    res += 1
if len(s) < 6:
    res += 6 - len(s) - res

print(res)

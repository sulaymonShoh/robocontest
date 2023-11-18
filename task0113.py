grade = int(input())

if grade >= 38:
    if grade % 5 >= 3:
        grade += 5 - grade % 5

print(grade)

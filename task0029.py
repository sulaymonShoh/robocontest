"""
29-masala

robocontest.uz/tasks/
"""

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
    
count = 0

for i in numbers:
    for k in range(2, i+1):
        if i%k==0 and k%2==0: count+=1
        continue
    print(count)
count=0
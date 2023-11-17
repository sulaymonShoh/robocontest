import math

writing = list(map(float, input().split()))
speaking = list(map(float, input().split()))
listening = float(input())
reading = float(input())

writing = math.floor(sum(writing) / 4)
speaking = math.floor(sum(speaking) / 4)
print((writing + speaking + listening + reading) / 4)
print(math.ceil((writing + speaking + listening + reading) / 4))

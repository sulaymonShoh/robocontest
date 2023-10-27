habc = list(map(int, input().split()))
word = input()
heights = []
for i in word:
    h = ord(i)-97
    heights.append(habc[h])
print(len(word)*max(heights))

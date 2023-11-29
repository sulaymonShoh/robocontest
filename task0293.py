text = input()
print(len(text))
for i in text:
    print(int(bin(ord(i))[2:]))

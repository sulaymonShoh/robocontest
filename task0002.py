sonlar = input().split()
a = int(sonlar[0])
b = int(sonlar[1])

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")

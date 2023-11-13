n = input()
b = n.find("1")
e = n.rfind("1")
print(["YES", "NO"]["0" in n[b : e + 1]])
# not finished

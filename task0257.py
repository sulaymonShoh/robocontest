n = input()
l = n.index("1")
r = n.rfind("1")
print(["NO", "YES"]["0" in n[l : r + 1]])

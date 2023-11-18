n = int(input())
a = 1

for i in range(0, n):
    for j in range(0, i + 1):
        print(f"{a}", end=" ")
        a += 1
    print()


# n = int(input())
# a = 1

# for i in range(0, n):
#     for i in range(0, i + 1):
#         print(f"{a: >2}", end=" ")
#         a += 1
#     print()

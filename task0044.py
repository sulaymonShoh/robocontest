y = int(input())
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
    print("Kabisa yili")
else: print("Kabisa yili emas")
# accepted
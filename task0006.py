y = "{:0>4}".format(int(input()))
y1=int(y)
if y1%400 == 0 or (y1%4 == 0 and y1%100 != 0): print(f"12/09/{y}")
else: print(f"13/09/{y}")
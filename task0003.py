with open("input.txt", "r") as fin:
	a = [int(i) for i in fin.readlines()]
	print(sum(a))	
with open('input.txt', 'r') as fin:
	a, b =  map(str, fin.read().split('\n'))
	a, b = a.split(' '), b.split(' ')
	a, b = [int(x) for x in a], [int(x) for x in b]

	if max(a[0], b[0]) == a[0]:
		a, b = b, a

	rh = b[0]-a[0]
	rm = b[1]-a[1]
	if rm<0: rm = 60+rm

	rs = b[2]-a[2]
	if rs<0: rs = 60+rs

	wt = rh*3600 + rm*60 + rs
	with open('output.txt', 'w') as fout:
		fout.write(str(wt))
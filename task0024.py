a = list(map(int, input().split()))
b = list(map(int, input().split()))

def time_interval(start, stop):
	res = 0
	hours = stop[0]-start[0]
	mins = stop[1]-start[1]
	seconds = stop[2]-start[2]

	res = hours * 3600 + mins * 60 + seconds
	return res

print(time_interval(a, b))
a, b=map(int, input().split(' '))
progress=0
days=0
for i in range(100):
	progress+=a
	print(f'{i+1}-kun: {progress}%')
	if progress>=100:
		days=i+1
		break
	else:
		progress-=b*3
print(days)
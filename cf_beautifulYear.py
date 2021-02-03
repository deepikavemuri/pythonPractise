n = int(input())
x = []
while True:
	n += 1
	x[:] = [int(i) for i in str(n)]
	if len(list(set(x))) == 4:
		print(''.join(str(i) for i in x))
		break
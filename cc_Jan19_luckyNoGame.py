t = int(input())
for i in range(t):
	inp = input().split()
	n = int(inp[0])
	a = int(inp[1])
	b = int(inp[2])
	ar = input().split()
	ar[:] = [int(x) for x in ar]
	while True:
		f = 0
		for i in ar:
			if a%i == 0 and f == 1:
				ar.remove(i)
				f = 0
				continue
			if b%i == 0 and f == 0:
				ar.remove(i)
				f = 1
				continue
			if a%i != 0 and f == 1:
				f = 2
			if b%i != 0 and f == 0:
				f = 3
		if f == 2:
			print("BOB")
			break
		if f == 3:
			print("ALICE")
			break
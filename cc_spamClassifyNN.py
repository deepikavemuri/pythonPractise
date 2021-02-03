t = int(input())
for _ in range(t):
	inp = input()
	inp = inp.split()
	n = int(inp[0])
	minX = int(inp[1])
	maxX = int(inp[2])
	WB = []
	for i in range(n):
		x = input().split()
		WB.append((int(x[0]), int(x[1])))
	
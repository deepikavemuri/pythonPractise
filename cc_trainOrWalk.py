t = int(input())
for i in range(t):
	(n, a, b, c, d, p, q, y) = map(int, input().split())
	x = map(int, input().split())
	if c in range(a, b+1) and d in range(a, b+1):
		d = 
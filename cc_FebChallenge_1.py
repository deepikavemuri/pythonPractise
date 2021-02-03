t = int(input())
for i in range(t):
	c = 0
	(n, a, b, k) = map(int, input().split())
	for j in range(1, n+1):
		if (j%a == 0 and j%b != 0) or (j%a != 0 and j%b == 0):
			c += 1
	if c >= k:
		print("Win")
	else:
		print("Lose")
t = int(input())
for _ in range(t):
	n = int(input())
	total = n*n
	for a in range(2, n+1):
		if a%2 != 0:
			x = n-a+1
			total += x*x
	print(total)
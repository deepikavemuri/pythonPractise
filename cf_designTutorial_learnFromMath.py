def composite(n):
	for i in range(2, n):
		if n%i == 0:
			return True
	return False

n = int(input())
f = 1
for i in range(n//2, 3,-1):
	if composite(i) and composite(n-i):
		print(i, n-i)
		break
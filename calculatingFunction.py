import math

n = int(input())
if n%2 == 0:
	print(math.ceil(n/2))
else:
	print(-math.ceil(n/2))
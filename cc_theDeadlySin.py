from math import gcd

t = int(input())
for _ in range(t):
	inp = input().split()
	x = int(inp[0])
	y = int(inp[1])
	print(gcd(x, y)*2)

	#while (x>0 or y>0) and x!=y:
	#	if x<y:
	#		y -= x
	#	else:
	#		x -= y
	#print(x+y)
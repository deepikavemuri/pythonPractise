from math import gcd
t = int(input())
for i in range(t):
	inp = input()
	inp = inp.split()
	n = int(inp[0])
	a = int(inp[1])
	k = int(inp[2])
	
	s = (n-2)*180
	d = (2*s - 2*a*n)
	x = a*n*(n-1)+(k-1)*d
	y = n*(n-1)
	temp = gcd(x,y)
	x = x//temp
	y = y//temp
	print(x, y)
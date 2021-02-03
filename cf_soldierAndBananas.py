inp = input().split()
k = int(inp[0])
n = int(inp[1])
w = int(inp[2])

tot = k * w*(w+1)//2 
if tot < n:
	print(0)
else:
	print(tot-n)
inp = input().split()
n = int(inp[0])
k = int(inp[1])
c = 0
for i in range(n):
	t = int(input())
	if t%k == 0:
		c += 1
print(c)
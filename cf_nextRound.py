inp = input().split()
n = int(inp[0])
k = int(inp[1])
ar = input().split()
ar[:] = [int(i) for i in ar]
c = 0
for i in range(len(ar)):
	if ar[i] >= ar[k-1] and ar[i] > 0:
		c += 1
print(c)
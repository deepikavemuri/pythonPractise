n = int(input())
ar = input().split()
ar[:] = [int(i) for i in ar]
ret = []
for i in range(len(ar)):
	c = 1
	for j in range(i, len(ar)-1):
		if ar[j] <= ar[j+1]:
			c += 1
		else:
			break
	ret.append(c)
print(max(ret))
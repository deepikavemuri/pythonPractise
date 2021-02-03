n = int(input())
ar = []
for i in range(n):
	ar.append(input())
c = 1
for i in range(len(ar)-1):
	if ar[i] != ar[i+1]:
		c += 1
print(c)
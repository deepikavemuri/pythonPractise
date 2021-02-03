n = int(input())
ar = []
for i in range(n):
	(x,y) = map(int, input().split())
	ar.append((x,y))
c = 0
for (i1,j1) in ar:
	for(i2,j2) in ar:
		if i1 != i2 and i1 == j2:
			c += 1
print(c)
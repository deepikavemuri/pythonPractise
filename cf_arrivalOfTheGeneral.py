n = int(input())
ar = input().split()
ar[:] = [int(i) for i in ar]
c = 0
maxS = ar.index(max(ar))
for i in range(maxS, 0, -1):
	t = ar[i-1]
	ar[i-1] = ar[i]
	ar[i] = t
x = ar[::-1]
minS = x.index(min(x))
print(maxS + minS)
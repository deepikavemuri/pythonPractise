(s,n) = map(int, input().split())
ar = []
for i in range(n):
	(x,y) = map(int, input().split())
	ar.append((x,y))
ar.sort()
f = 1
for (i,j) in ar:
	if s > i:
		s += j
	else:
		print("NO")
		f = 0
		break
if f == 1:
	print("YES")
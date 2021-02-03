x = int(input())
l = list(map(int, input().split()))

ind = l.index(max(l))
c = 0
while l[ind] > x - 1:
	l[ind] = l[ind] - x
	for i in range(len(l)):
		if i != ind:
			l[i] -= 1
	c += 1
print(c)
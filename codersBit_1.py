a = [1,2,3]
subLists = []
for i in range(len(a)):
	for j in range(i, len(a)):
		sub = a[i:j+1]
		subLists.append(sub)

print(subLists)
sums = []
for i in subLists:
	sums.append(sum(i))
f = 0
c = 0
for elem in sums:
	if elem == 2:
		c += 1
	else:
		f = 0
		for x in range(2,elem):
			if elem%x == 0:
				f = 0
				break
			else:
				f = 1
		if f == 1:
			c += 1
print(c)
def stringRotate(x):
	return (x[1:] + x[:1])

A = ["aba", "ababa", "a"]
eq = []
for i in A:
	c = 0
	x = i
	for j in range(len(i)):
		if i != stringRotate(x):
			x = stringRotate(x)
			print(x)
			c += 1
			print(c)
		else:
			eq.append(c)
print(max(a))
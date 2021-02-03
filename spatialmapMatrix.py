inp = input()
inp = inp.split()
n1 = int(inp[0])
m1 = int(inp[1])
a = []
for i in range(n1):
	r1 = input()
	r1 = r1.split()
	r2 = []
	for i in r1:
		r2.append(int(i))
	a.append(r2)
c = 0
for j in range(len(a)):
	land = 0
	for i in range(len(a)):
		if a[i][j] != 0:
			print(a[i][j])
	c += 1
print(c)
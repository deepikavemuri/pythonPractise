A = [1,2,3]
B = [[1,2,78], [1,3,0], [2,4,10]]
for b in B:
	if b[0] == 1:
		A[b[1]-1] = b[2]
		print(A)
	if b[0] == 2:
		c = 0
		divisors = []
		for i in range(b[1], b[2]):
			divisors = [x for x in range(2,i) if i%x == 0]
			if len(divisors)%2 == 0:
				for j in A:
					i = i-j
					divisors = [x for x in range(2,i) if i%x == 0]
					if len(divisors)%2 != 0:
						c += 1
						break
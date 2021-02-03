ar = []
for i in range(5):
	temp = input().split()
	temp[:] = [int(i) for i in temp]
	ar.append(temp)
for i in range(len(ar)):
	for j in range(len(ar)):
		if ar[i][j] == 1:
			x = i+1
			y = j+1
			break
print(abs(x-3) + abs(y-3))
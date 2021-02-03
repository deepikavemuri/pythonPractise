A = [39,99,70,24,49,13,86,43,88,74,45,92,72,71,90,32,19,76,84,46,63,15,87,1,39,58,17,65,99,43,83,29,64,67,100,14,17,100,81,26,45,40,95,94,86,2,89,57,52,91,45]
B = [1221,360,459,651,958,584,345,181,536,116,1310,403,669,1044,1281,711,222,280,1255,257,811,409,698,74,838]

subLists = []
for i in range(len(A)):
	for j in range(i, len(A)):
		sub = A[i:j+1]
		subLists.append(sub)
G = []
for i in subLists:
	G.append(max(i))
print(G)
for i in range(len(G)):
	y = []
	prod = 1
	for j in range(1,G[i]+1):
		if G[i]%j == 0:
			y.append(j)
	for k in y:
		prod *= k
	G[i] = prod
print(G)
G.sort(reverse=True)
print(G)

X = []
for j in B:
	X.append(G[j-1])
print(X)
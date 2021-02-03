n = int(input())
maxi = 0
ar =[]
for i in range(n):
	(a,b) = map(int, input().split())
	ar.append(abs(a-b))
print(ar.index(max(ar)), max(ar))
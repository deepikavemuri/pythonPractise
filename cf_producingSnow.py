n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))
for i in range(n):
	remain = 0
	for j in range(i+1):
		snow = min(v[j], t[i])
		v[j] -= snow
		remain += snow
	print(remain, end = " ")
t = int(input())
for i in range(t):
	n = int(input())
	s = []
	for i in range(n):
		s1 = set(input())
		s.append(s1)
	x = s[0]
	for j in s:
		x = x & j
	print(len(x))
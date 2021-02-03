A = 1
B = 1
C = 7
D = 7

x = C-A
s = 0
if x%2 != 0:
	temp = 1
	while temp<x:
		s += 4*temp
		temp += 2
else:
	temp = 0
	while temp<x:
		s += 4*temp
		temp += 2
	s += 1
print(s)
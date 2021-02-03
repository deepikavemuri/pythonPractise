ar = input().split('+')
ar[:] = [int(i) for i in ar]
s = ""
ar.sort()
for i in ar:
	s += str(i) + "+"
print(s[:-1])
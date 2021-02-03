def parent(a):
	live = exists(a)
	if live != -1:
		return live[0]
	return a

def exists(a):
	for i in dsu:
		if a in i:
			return i
	return -1

def add(a, b):
	live = exists(a)
	live.append(b)

n = int(input())
v = input()
t = input()
dsu = []
spells = []
for i in range(n):
	s = []
	if parent(v[i]) != parent(t[i]):
		if exists(v[i]) != -1:
			add(v[i], t[i])
		elif exists(t[i]) != -1:
			add(t[i], v[i])
		else:
			s.extend([v[i], t[i]])
			dsu.append(s)
		spells.append((t[i], v[i]))

print(len(spells))
for i in spells:
	print(i[0], i[1])
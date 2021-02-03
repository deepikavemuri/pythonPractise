a = input()
if a[1:-1] == '':
	print(0)
else:
	a = list(set(a[1:-1].split(', ')))
	print(len(a))
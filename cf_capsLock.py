n = input()
if (n[0].islower() and n[1:].isupper()) or n.isupper():
	print(n.lower().capitalize())
else:
	print(n)
n = input()
f = 0

def isLucky(n):
	if ('4' in n or '7' in n) and len(n) == 1:
		return True
	elif '4' in n and '7' in n:
		return True
	return False

if isLucky(n):
	print("YES")
else:
	for i in range(int(n)):
		if n%i == 0 and isLucky(i):
			print("YES")
			f = 1
			break
if f == 0:
	print("NO")
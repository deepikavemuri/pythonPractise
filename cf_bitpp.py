t = int(input())
x = 0
for i in range(t):
	n = input()
	if '+' in n:
		x += 1
	if '-' in n:
		x -= 1
print(x)
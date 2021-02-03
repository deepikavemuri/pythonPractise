t = int(input())
for i in range(t):
	top = input()
	bottom = input()
	if (top[0] == 'o' or bottom[0] == 'o') and (top[1] == 'b' or bottom[1] == 'b') and (top[2] == 'b' or bottom[2] == 'b'):
		print("yes")
	elif (top[0] == 'b' or bottom[0] == 'b') and (top[1] == 'o' or bottom[1] == 'o') and (top[2] == 'b' or bottom[2] == 'b'):
		print("yes")
	elif (top[0] == 'b' or bottom[0] == 'b') and (top[1] == 'b' or bottom[1] == 'b') and (top[2] == 'o' or bottom[2] == 'o'):
		print("yes")
	else:
		print("no")
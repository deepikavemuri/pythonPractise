for i in range(5):
	temp = list(map(int, input().split()))
	if 1 in temp:
	    x = temp.index(1)
	    y = i
	    break
print(abs(x-2) + abs(y-2))
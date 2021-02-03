str = input()
x = []
for i in range(len(str)):
	for j in range(i+1, len(str)):	
		x.append(str[:i] + str[j] + str[i+1:j] + str[i] + str[j+1:])
x = list(set(x))
print(len(x))
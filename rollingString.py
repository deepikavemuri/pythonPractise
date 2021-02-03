def shiftR(start, stop, s):
	s1 = list(s)
	s3 = []
	for i in range(len(s1)):
		if i >= int(start) and i <= int(stop): 
			y = ord(s1[i])
			if y == 122:
				y = 97
			else:
				y += 1
			z = chr(y)
			s3.append(z)

		else:
			s3.append(s1[i])
	return("".join(s3))

def shiftL(start, stop, s):
	s1 = list(s)
	s3 = []
	
	for i in range(len(s1)):
		if i >= int(start) and i <= int(stop): 
			y = ord(s1[i])
			if y == 97:
				y = 122
			else:
				y -= 1
			z = chr(y)
			s3.append(z)

		else:
			s3.append(s1[i])

	return("".join(s3))


def rollingString(s, operations):
    x = []
    for i in operations:
        x = i.split(" ")
        if x[2] == 'L':
        	return(shiftL(x[0], x[1], s))

        else:
        	return(shiftR(x[0], x[1], s))

s = input()

print(rollingString(s, ["0 0 L"]))
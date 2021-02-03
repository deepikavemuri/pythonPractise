text = input()
ret = ""
for i in range(len(text)):   
	if text[0].isupper():
		ret.append(text[0].lower())
	elif text[i] == '_' or text[i] == '-':
		ret.append(text[i].upper())
	else:
		ret.append(text[i])
print(text)
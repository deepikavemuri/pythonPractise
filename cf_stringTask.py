n = input()
n = n.lower()
s = ""
vowels = "aoyeui"
for i in n:
	if i not in vowels:
		s += "." + i
print(s)
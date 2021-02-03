n = int(input())
seq = input()
c = 0
f = 0
while c < n:
	for i in range(len(seq)-1):
		if seq[i] == seq[i+1]:
			c += 1
			f = 0
			print(seq)
			seq = seq.replace(seq[i], "")
			break
		else:
			f = 1
	if f == 1:
		break
print(c)
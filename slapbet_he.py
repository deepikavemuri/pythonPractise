n = int(input())
out = []

for i in range(n):
	x = input()
	bt1, bt2, mt1, mt2 = x.split(" ")
	bt1 = int(bt1)
	bt2 = int(bt2)
	mt1 = int(mt1)
	mt2 = int(mt2)
	if bt2-bt1 == 1 and mt2-mt1 == 1:
		if bt2 == mt1:
			out.append("Point")
		else:
			out.append("Line")

	else:
		out.append("Nothing")

for i in out:
	print(i)
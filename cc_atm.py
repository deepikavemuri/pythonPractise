inp = input().split()
amount = int(inp[0])
bal = float(inp[1])
if amount%5 == 0 and bal-amount>0:
	print("{0:.2f}".format(bal-amount-0.5))
else:
	print("{0:.2f}".format(bal))
hosted = [2010, 2015,2016,2017,2019]
T = int(input())
for i in range(T):
	n = int(input())
	if n in hosted:
		print("HOSTED")
	else:
		print("NOT HOSTED")
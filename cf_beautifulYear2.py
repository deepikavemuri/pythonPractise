def hasDistinctDigits(n):
    x = str(n)
    return list(sorted(set(x))) == list(sorted(x))

n = int(input())
n += 1
while(hasDistinctDigits(n) == False):
	n += 1
print(n)

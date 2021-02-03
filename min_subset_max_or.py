ar = list(map(int, input().split()))
max_or = 0
for i in ar:
	max_or |= i
print(max_or)
pots = list(map(int, input().split(',')))
chance = 'A'
aCoins = 0

while len(pots) > 0:
	if chance == 'A':
		curMax = max(pots[0], pots[-1])
		aCoins += curMax
		del(pots[pots.index(curMax)])
		chance = 'B'
	else:
		curMax = max(pots[0], pots[-1])
		del(pots[pots.index(curMax)])
		chance = 'A'
print(aCoins)
n, k, q = map(int, input().split())
temps = []

for i in range(n):
    recipeRange = list(map(int, input().split()))
    temps.extend(list(range(recipeRange[0], recipeRange[1]+1)))

admissibleTemps = []
for i in set(temps):
    if temps.count(i) >= k:
        admissibleTemps.append(i)

for i in range(q):
    query = list(map(int, input().split()))
    c = 0
    queryTemps = list(range(query[0], query[1]+1))
    for i in queryTemps:
        if i in admissibleTemps:
            c += 1
    print(c)

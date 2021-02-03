n = int(input())
measures = []
for i in range(n):
	measure = list(map(int, input().split()))
	measures.append(measure)

mini = 0

for j in range(1, len(measures)):
	for i in range(1, len(measures)):
		if measures[i][0] < measures[mini][0] and measures[i][1] < measures[mini][1] and measures[i][2] < measures[mini][2]:  
			mini = i

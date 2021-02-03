l = {'d', 'f'}
r = {'j', 'k'}
words = []
time = []
t = 0.2
N = int(input())
for i in range(N):
	f = 0	
	x = input()
	for i in range(len(words)):
		if words[i] == x:
			t += time[i]/2;
			f = 1
	if f == 0:
		words.append(x)
			
	for i in range(len(x)-1):
		if x[i] in l:
			if x[i+1] in l:
				t += 0.4 
			else:
				t += 0.2
		else:
			if x[i+1] in r:
				t += 0.4
			else:
				t += 0.2
	time.append(t)	
print(t)
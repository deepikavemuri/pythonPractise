n = int(input())
ar = input().split()
ar[:] = [int(i) for i in ar]
a = []
for i in range(n):
	a.append(0)
for i in range(len(ar)):
	a[ar[i]-1] = i+1
for i in a:
	print(i, end=" ") 
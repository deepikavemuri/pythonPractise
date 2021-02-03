def mergeSort(ar, l, h):
	if l<h:
		mid = (l+h)//2
		mergeSort(ar, l, mid)
		mergeSort(ar, mid+1, h)
		merge(ar, l, mid, h)

def merge(ar, l, mid, h):
	i = l
	j = mid+1
	c = 0
	C = []
	for i in range(h-l+1):
		C.append(0)

	while i<=mid and j<=h:
		if ar[i] < ar[j]:
			C[c] = ar[i]
			c += 1
			i += 1
		else:
			C[c] = ar[j]
			c += 1
			j += 1
	while i <= mid:
		C[c] = ar[i]
		c += 1
		i += 1
	while j <= h:
		C[c] = ar[j]
		c += 1
		j += 1

	for x in range(l, h+1):
		ar[x] = C[x-l]


ar = input().split()
ar[:] = [int(i) for i in ar]
mergeSort(ar, 0, len(ar)-1)
print(ar)
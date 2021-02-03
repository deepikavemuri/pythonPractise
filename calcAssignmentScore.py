ar = map(int, input().split())
ar = sorted(ar, reverse = True)
avg = sum(ar[:9])/8
print(avg*25/100)
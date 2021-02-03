s1 = input()
s2 = input()
s3 = sorted(input())
s4 = sorted(s1 + s2)
if s3 == s4:
	print("YES")
else:
	print("NO")
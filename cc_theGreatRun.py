t = int(input())
for i in range(t):
    a = input()
    a = a.split()
    n = int(a[0])
    k = int(a[1])
    x = input()
    x = x.split()
    y = []
    for i in x:
        y.append(int(i))
    b = []
    for i in range(n):
    	b.append(sum(y[i:k+i]))

    print(max(b))
x = input().split()
r = range(0,len(x))
for i in r:
    x[i] = int(x[i])

if x[0] - x [1] == x[1] - x[2] :
    print(x[len(x)-1] + x[1] - x[0])

if(x[1]/x[0] == x[2]/x[1]):
    print(x[len(x)-1] )

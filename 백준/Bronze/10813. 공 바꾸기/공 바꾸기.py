n,m = map(int,input().split())
x=[0]*(n+1)
for i in range(0,n+1):
    x[i] = i
    

for i in range(m):
    a,b=map(int,input().split())
    tmp = 0
    tmp = x[a]
    x[a] = x[b]
    x[b] = tmp

for i in range(1,n+1):
    print(x[i],end=" ")
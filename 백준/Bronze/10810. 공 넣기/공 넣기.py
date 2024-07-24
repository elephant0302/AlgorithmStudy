n,m = map(int,input().split())
n_list = [0]*n

for _ in range(m):
    a,b,c=map(int,input().split())
    for i in range(a-1,b):
        n_list[i] = c

for i in range(n):
    print(n_list[i], end=" ")
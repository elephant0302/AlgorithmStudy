a,b = map(int,input().split())
n = int(input())
m = int(input())

if a*m + b <= n*m and a <= n:
    print(1)
else:
    print(0)
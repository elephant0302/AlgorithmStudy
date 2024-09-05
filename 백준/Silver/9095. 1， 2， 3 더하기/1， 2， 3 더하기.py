n = int(input())
nlist = [0]*(n+1)
for i in range(1,n+1):
    nlist[i] = int(input())

nmax = max(nlist)


dp = [0]*1000000


for i in range(1,nmax+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    elif i >= 4:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(n):
    print(dp[nlist[i+1]])
    
    
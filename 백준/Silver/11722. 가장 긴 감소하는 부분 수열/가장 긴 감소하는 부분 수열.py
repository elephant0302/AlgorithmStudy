dp = [1] * 10000
n = int(input())

nlist = list(map(int,input().split()))

for i in range(n):
    for j in range(i):
        if nlist[j] > nlist[i]:
            dp[i] = max(dp[i],dp[j]+1)
            
print(max(dp))
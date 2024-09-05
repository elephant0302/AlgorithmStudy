n = int(input())

dp = [0]*(n+2)
dp[0] = 0
dp[1] = 1

for i in range(n):
    dp[i+2] = dp[i+1] + dp[i]

print(dp[n])
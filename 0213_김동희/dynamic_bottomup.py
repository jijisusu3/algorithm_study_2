# 피보 수열 / 보텀업 dp

# 0 ~ 99까지라면,
dp = [0]*100

dp[1] = 1
dp[2] = 1
n = 99

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
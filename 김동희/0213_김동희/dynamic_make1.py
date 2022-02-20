# 하나의 값을 계속해서 2,3,5로 나눈값에서 1을 뺄때, 1이 되는 그 횟수를 찾기 / 보텀업

x =  26

dp = [0] * 30001

for i in range(2, x+1):
    # 현재 수에서 1을 뺴는 경우
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 5 == 0:
        dp[i] = min(dp[i],dp[i//5]+1)
print(dp[x])
        
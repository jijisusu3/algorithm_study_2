# 피보 수열 / 탑다운 dp

# 0 ~ 99까지라면,
dp = [0]*100

def fibo(x):
    # 종료조건
    if x ==1 or x==2:
        return 1
    if dp[x] != 0:
        dp[x]
        
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]
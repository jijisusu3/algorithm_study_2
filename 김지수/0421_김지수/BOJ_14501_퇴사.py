N = int(input())
T, P = [], []
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i + 1]  # 상담 안하고 넘어감, 이전의 값 가져오기
    else:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
        # 현재 가격과 이 상담을 선택했을 때 다음 선택의 최대값 vs 이거 안넣었을 때 최대값
print(dp[0])

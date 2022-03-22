import sys; sys.stdin = open('4012.txt')

def synergy(x):
    cnt = 0
    for i in x:
        for j in x:
            if i != j:
                cnt += arr[i][j]
    return cnt

def dfs(x):
    global ans
    if x == N // 2:
        A = []
        B = []
        for i in range(N):
            if visit[i]:
                A.append(i)
            else:
                B.append(i)
        if abs(synergy(A) - synergy(B)) < ans:
            ans = abs(synergy(A) - synergy(B))
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            dfs(x + 1)
            visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 9999999999
    visit = [0 for _ in range(N)]

    dfs(0)
    print('#{} {}'.format(tc, ans))
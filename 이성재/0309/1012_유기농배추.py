import sys; sys.stdin = open('1012.txt')

def dfs(x, y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if arr[ny][nx] == 1:
                arr[ny][nx] = 2
                dfs(nx, ny)

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    cnt = 0
    for x in range(M):
        for y in range(N):
            if arr[y][x] == 1:
                dfs(x, y)
                cnt += 1
    
    print(cnt)
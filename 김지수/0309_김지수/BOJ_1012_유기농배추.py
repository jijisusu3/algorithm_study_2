import sys
sys.setrecursionlimit(10000)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (0 <= nr < N) and (0 <= nc < M):
            if arr[nr][nc] == 1:
                arr[nr][nc] = -1
                dfs(nr, nc)


TC = int(input())
for tc in range(1, TC + 1):
    cnt = 0
    N, M, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                dfs(r, c)
                cnt += 1
    print(cnt)





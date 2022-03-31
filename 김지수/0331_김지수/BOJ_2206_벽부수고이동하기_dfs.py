import sys
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1] # 상하좌우


def dfs(row, col, wall_cnt, cnt, arrive):
    global result
    if wall_cnt > 1:
        return
    if arrive == 1:
        if cnt < result:
            result = cnt
        return
    if cnt > result:
        return
    for i in range(4):
        nr, nc = row + dr[i], col + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc] == 0:
                if nr == N - 1 and nc == M - 1:
                    dfs(nr, nc, wall_cnt, cnt + 1, 1)
                if arr[nr][nc] == 1:
                    visited[nr][nc] = 1
                    dfs(nr, nc, wall_cnt + 1, cnt + 1, 0)
                    visited[nr][nc] = 0
                if arr[nr][nc] == 0:
                    visited[nr][nc] = 1
                    dfs(nr, nc, wall_cnt, cnt + 1, 0)
                    visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = (N * M) + 1
dfs(0, 0, 0, 1, 0)
if result != (N * M) + 1:
    print(result)
else:
    print(-1)
import sys; sys.stdin = open('7576.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(a, b):
    global cnt
    if graph[a][b] == cnt:
        cnt += 1
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < M and 0 <= y < N:
            if graph[x][y] == 0:
                graph[x][y] = cnt
                dfs(x, y)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

cnt = 1

for i in range(N):
    for j in range(M):
        if graph[j][i] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)

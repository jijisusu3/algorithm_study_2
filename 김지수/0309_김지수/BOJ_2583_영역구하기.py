import sys
sys.setrecursionlimit(10000)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(y, x, cnt):
    arr[y][x] = 1
    for dr, dc in d:
        ny, nx = y + dr, x + dc
        if (0 <= ny < M) and (0 <= nx < N) and arr[ny][nx] == 0:
            cnt = dfs(ny, nx, cnt + 1)
    return cnt


M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
result = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] == 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            result.append(dfs(i, j, 1))


print(len(result))
print(result)

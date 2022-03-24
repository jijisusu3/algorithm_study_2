dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(row, col, X):
    if len(X) == 6:
        if X not in result:
            result.append(X)
        return
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            DFS(nr, nc, X + arr[nr][nc])


arr = [input().split() for _ in range(5)]
result = []
for r in range(5):
    for c in range(5):
        DFS(r, c, arr[r][c])
print(len(result))
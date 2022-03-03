N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    global count
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 1:
                count += 1
                arr[nr][nc] = 0
                bfs(nr, nc)


result = []
for r in range(N):
    for c in range(N):
        count = 0
        if arr[r][c] == 1:
            count += 1
            arr[r][c] = 0
            bfs(r, c)
        if count != 0:
            result.append(count)
result = sorted(result)
print(len(result))
for i in result:
    print(i)



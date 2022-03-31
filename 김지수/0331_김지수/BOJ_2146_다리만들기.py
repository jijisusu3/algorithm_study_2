from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def land(row, col):
    global cnt
    Q = deque()
    Q.append((row, col))
    while Q:
        a, b = Q.popleft()
        arr[a][b] = cnt
        for i in range(4):
            nr = a + dr[i]
            nc = b + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if arr[nr][nc] == 1:
                    visited[nr][nc] = 1
                    arr[nr][nc] = cnt
                    Q.append((nr, nc))


def bridge(label):
    global result, visited
    Q2 = deque()
    for x in range(N):
        for y in range(N):
            if arr[x][y] == label:
                Q2.append((x, y))
                visited[x][y] = 0
    while Q2:
        c, d = Q2.popleft()
        for i in range(4):
            nr = c + dr[i]
            nc = d + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                # 다른 땅 만났을 때
                if arr[nr][nc] != 0 and arr[nr][nc] != label:
                    result = min(result, visited[c][d])
                    return
                # 바다 만났을 때
                if arr[nr][nc] == 0 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[c][d] + 1
                    Q2.append((nr, nc))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 1
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0 and arr[r][c] == 1:
            visited[r][c] = 1
            land(r, c)
            cnt += 1

visited = [[-1] * N for _ in range(N)]  # 다시 기록해야하므로 visited
result = N ** 2
for i in range(1, cnt):
    bridge(i)
print(result)

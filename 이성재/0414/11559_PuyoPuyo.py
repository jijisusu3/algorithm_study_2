import sys; sys.stdin = open('123.txt')
from collections import deque
arr = [list(input()) for _ in range(12)]
N, M = 12, 6
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global ans

    rst = 0
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '.' and visit[i][j] == 0:
                q = deque()
                q.append((i, j))
                stack = [(i, j)]
                while q:
                    x, y = q.popleft()
                    visit[x][y] = 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                            if arr[nx][ny] == arr[i][j]:
                                q.append((nx, ny))
                                visit[nx][ny] = 1
                                stack.append((nx, ny))
                if len(stack) >= 4:
                    while stack:
                        x, y = stack.pop()
                        arr[x][y] = '.'
                        rst = 1
    if rst == 1:
        ans += 1
        down()
        bfs()

def down():
    for i in range(N - 2, -1, -1):
        for j in range(M - 1, -1, -1):
            if arr[i][j] != '.' and arr[i + 1][j] =='.':
                q = [(i, j)]
                while q:
                    x, y = q.pop()
                    if x + 1 < N and arr[x + 1][y] == '.':
                        arr[x + 1][y] = arr[x][y]
                        arr[x][y] = '.'
                        q.append((x + 1, y))

bfs()
print(ans)
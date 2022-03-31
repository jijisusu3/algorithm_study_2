import sys; sys.stdin = open('123.txt') #...
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visit[x][y] = 1
    arr[x][y] = k
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visit[nx][ny] == 0 and arr[nx][ny] == 1:
                dfs(nx, ny)

def bfs(a):
    global ans
    rst = [[0] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == a:
                q.append((i, j))
                rst[i][j] = 1
    
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if rst[nx][ny] != a:
                    ans = min(ans, rst[x][y])
                    return
                
                if rst[nx][ny] == 0 and arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

ans = 999999999
k = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visit[i][j] == 0:
            dfs(i, j)
            k += 1

for i in range(1, k + 1):
    bfs(i)

print(ans)
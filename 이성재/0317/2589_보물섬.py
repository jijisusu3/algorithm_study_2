import sys; sys.stdin = open('2589.txt')
from collections import deque

def bfs(a, b):
    Q.append([a, b])
    visit = [[0] * m for _ in range(n)]
    ans = 0
    visit[a][b] = 1

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 'L' and visit[nx][ny] == 0:
                    Q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1
                    ans = max(ans, visit[nx][ny])
    return ans - 1

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
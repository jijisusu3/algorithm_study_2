import sys; sys.stdin = open('2667.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(a, b):
    global cnt
    visited[a][b] = True
    if graph[a][b] == 1:
        cnt += 1
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < N:
            if visited[x][y] == False and graph[x][y] ==1:
                dfs(x, y)

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

cnt = 0
result = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] == 1:
            dfs(i, j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i)
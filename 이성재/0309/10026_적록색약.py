import sys; sys.stdin = open('10026.txt')

def dfs(x, y, a):
    list_a.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in list_a:
            if a == 0 and color[nx][ny] == color[x][y]:
                dfs(nx, ny, 0)
            elif a == 1 and color[nx][ny] == color[x][y]:
                dfs(nx, ny, 1)

N = int(input())
color = [list(input()) for _ in range(N)]

list_a = []
cnt_0 = 0

for i in range(N):
    for j in range(N):
        if (i, j) not in list_a:
            dfs(i, j, 0)
            cnt_0 += 1

for i in range(N):
    for j in range(N):
        if color[i][j] == 'R':
            color[i][j] = 'G'

list_a = []
cnt_1 = 0
for i in range(N):
    for j in range(N):
        if (i, j) not in list_a:
            dfs(i, j, 1)
            cnt_1 += 1

print(cnt_0, cnt_1)
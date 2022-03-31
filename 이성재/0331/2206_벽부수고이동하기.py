import sys; sys.stdin = open('123.txt') # 틀림..

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    q = []
    q.append([0, 0])
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    check = 0
    while q:
        x, y = q.pop()
        if x == N - 1 and y == M - 1:
            return visit[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and check == 0:
                    check += 1
                    visit[nx][ny] = visit[x][y] + 1
                    q.append([nx, ny])
                elif arr[nx][ny] == 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append([nx, ny])

    return -1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(bfs())
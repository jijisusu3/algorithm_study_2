# 아이디어
# 다른 섬이 아닌, 자기 자신이랑 연결되는 경우는 어떻게 해결?
# 각각 다른 숫자로 변환
# BFS 활용하여 다른 섬 도착했을 때 최소값을 도출
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(n):
    global cnt
    visit = [[0] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == n:
                q.append((i, j))
                visit[i][j] = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > 0 and arr[nr][nc] != n:
                    if cnt > visit[r][c]:
                        cnt = visit[r][c]
                        return
                    return

                if arr[nr][nc] == 0 and visit[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    q.append((nr, nc))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = N*N

number = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            q = deque()
            q.append((i, j))
            arr[i][j] = number

            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                        arr[nr][nc] = number
                        q.append((nr, nc))
            number += 1

for i in range(2, number):
    BFS(i)

result = cnt-1
print(result)
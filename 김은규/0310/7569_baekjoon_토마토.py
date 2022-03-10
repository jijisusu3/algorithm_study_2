from collections import deque

def bfs(arr, visited):
    while lst:
        i, j, k = lst.popleft()

        for x in range(6):
            ni, nj, nk = i + di[x], j + dj[x], k + dk[x]
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M:
                if arr[ni][nj][nk] == 0 and visited[ni][nj][nk] == 0:
                    arr[ni][nj][nk] = 1
                    visited[ni][nj][nk] = visited[i][j][k] + 1  # 하루에 1씩 증가하고, 마지막에 최대 일수 구하기 위해서
                    lst.append([ni, nj, nk])

    max_v = -2
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1

                elif visited[i][j][k] > max_v:
                    max_v = visited[i][j][k]

    return max_v

di = [0, 0, 0, 0, -1, 1]
dj = [0, 1, 0, -1, 0, 0]
dk = [-1, 0, 1, 0, 0, 0]

M, N, H = map(int, input().split())  # 가로 M, 세로 N, 높이 H
arr = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for __ in range(H)]
lst = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                lst.append([i, j, k])

print(bfs(arr, visited))

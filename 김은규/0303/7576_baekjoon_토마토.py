# 아이디어
# visited 배열과 arr 배열을 비교하여 둘 다 0인 경우만 진행되도록 설정
# 시간초과....... -> deque로 해결!!!

from collections import deque

def bfs(arr, visited):
    while lst:
        i, j = lst.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    arr[ni][nj] = 1
                    visited[ni][nj] = visited[i][j] + 1  # 하루에 1씩 증가하고, 마지막에 최대 일수 구하기 위해서
                    lst.append([ni, nj])

    max_v = -2
    for k in range(N):
        for m in range(M):
            if arr[k][m] == 0:
                return -1

            elif visited[k][m] > max_v:
                max_v = visited[k][m]

    return max_v

M, N = map(int, input().split())  # 가로 M, 세로 N
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
lst = deque([])


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            lst.append([i,j])

print(bfs(arr, visited))
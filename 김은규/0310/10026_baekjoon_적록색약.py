import sys; sys.stdin = open('10026.txt', 'r')
from collections import deque

# 아이디어
# BFS를 활용. 적록색약의 경우와 아닌 경우 2번 BFS 적용.
# 2차원 배열의 좌표를 하나씩 구해서 상하좌우를 옮겨가며 이전 좌표와 같을 경우 visited에 1 표시 후 q에 추가
# 아닌 경우 q에 추가하지 않음으로 while문 종료.


def BFS(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and arr[i][j] == arr[ni][nj]:
                    visited[ni][nj] = 1
                    q.append([ni,nj])

N = int(input())
arr = [list(input()) for _ in range(N)]
cnt_1 = 0  # 적록색약 x
cnt_2 = 0  # 적록색약 o

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt_1 += 1
            BFS(i, j)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt_2 += 1
            BFS(i, j)

print(cnt_1, cnt_2)




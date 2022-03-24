from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(n):
    Q = deque()
    Q.append((row, col))
    while Q:



num = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            num += 1


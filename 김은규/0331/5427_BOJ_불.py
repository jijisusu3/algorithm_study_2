# 아이디어
# 불과 사람 BFS 따로 진행..??
# 출구를 찾고 거기서 bfs를 실행해서 사람과 불을 같이 찾을까??
# '.' : 빈 공간
# '#' : 벽
# '@' : 상근이 위치
# '*' : 불

import sys; sys.stdin = open('5427.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(i, j):
    global person, fire
    q = deque()
    q.append((i, j))
    visit[i][j] = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < h and 0 <= nc < w and visit[nr][nc] == 0:
                if arr[nr][nc] == '.':
                    visit[nr][nc] = visit[r][c] + 1
                    q.append((nr, nc))

                if arr[nr][nc] == '@':
                    visit[nr][nc] = visit[r][c] + 1
                    person = visit[nr][nc]


                if arr[nr][nc] == '*':
                    visit[nr][nc] = visit[r][c] + 1
                    fire = visit[nr][nc]

T = int(input())
for tc in range(T):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    person = fire = 0xfffff

    for i in range(h):
        for j in range(w):
            if arr[i][0] == '.':
                bfs(i, 0)

            elif arr[i][w-1] == '.':
                bfs(i, w-1)

            elif arr[0][j] == '.':
                bfs(0, j)

            elif arr[h-1][j] == '.':
                bfs(h-1, j)

    if person < fire:
        print(person)
    else:
        print('IMPOSSIBLE')


# def BFS(i, j):
#     q = deque()
#     q.append((i, j))
#     visit[i][j] = 1
#
#     while q:
#         r, c = q.popleft()
#         for k in range(4):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < h and 0 <= nc < w and visit[nr][nc] == 0:
#                 if arr[nr][nc] == '.':
#                     visit[nr][nc] = visit[r][c] + 1
#                     q.append((nr, nc))
#
#
# def FIRE(i, j):
#     pass
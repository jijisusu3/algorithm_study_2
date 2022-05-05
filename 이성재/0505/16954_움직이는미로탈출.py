import sys; sys.stdin=open('123.txt')
from collections import deque

dx = [0, -1, 0, 1, 1, -1, -1, 1, 0]
dy = [1, 0, -1, 0, 1, -1, 1, -1, 0]

def bfs(x, y):

    q = deque()
    q.append((x, y))
    time = 0

    while q:
        x, y = q.popleft()
        
        for i in range(9):
            cnt = 0
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 8 and [nx, ny] not in wall:
                for j in range(len(wall)):
                    if wall[j][0] == 7:
                        cnt += 1
                if cnt == len(wall):
                    return 1
                if nx == 0 and ny == 7:
                    return 1
                
                q.append((nx, ny))
        for j in range(len(wall)):
            if wall[j][0] < 7:
                wall[j][0] += 1
        time += 1
        if time == 8:
            return 1
    return 0

arr = [list(input()) for _ in range(8)]
wall = []
for i in range(8):
    for j in range(8):
        if arr[i][j] == '#':
            wall.append([i, j])

print(bfs(7, 0))
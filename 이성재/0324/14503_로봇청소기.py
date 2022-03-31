import sys; sys.stdin = open('14503.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def direction(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    else:
        return 2

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 1
arr[r][c] = 2
while 1:
    dir = d
    for i in range(4):
        a = 0
        dir = direction(dir)
        nr = r + dx[dir]
        nc = c + dy[dir]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            cnt += 1
            r = nr
            c = nc
            arr[nr][nc] = 2
            d = dir
            a = 1
            break
    if a == 0:
        if d == 0:
            r += 1
        elif d == 1:
            c -= 1
        elif d == 2:
            r -= 1
        else:
            c += 1
        if arr[r][c] == 1:
            break
print(cnt)
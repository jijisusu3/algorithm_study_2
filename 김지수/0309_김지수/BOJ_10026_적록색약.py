import sys
sys.setrecursionlimit(1000000)

N = int(input())
arr = [list(input()) for _ in range(N)]
v = [[0]*N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def area(row, col):
    v[row][col] = 1
    temp = arr[row][col]
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (0 <= nr < N) and (0 <= nc < N):
            if v[nr][nc] == 0 and arr[nr][nc] == temp:
                area(nr, nc)


# 색약 아닐 때
cnt_1 = 0
for r in range(N):
    for c in range(N):
        if v[r][c] == 0:
            area(r, c)
            cnt_1 += 1

# 색약일때
cnt_2 = 0
v = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 'R':
            arr[r][c] = 'G'

for r in range(N):
    for c in range(N):
        if v[r][c] == 0:
            area(r, c)
            cnt_2 += 1

print(cnt_1, cnt_2)


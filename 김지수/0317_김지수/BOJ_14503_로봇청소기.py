
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1] # 북동남서 0 1 2 3


def robot(row, col, direction):
    global result
    if arr[row][col] == 0:
        arr[row][col] = 2
        result += 1 # 청소
    for _ in range(4):
        new_d = (direction + 3) % 4 # 처음 방향부터 ~ ...0 1 2 3 반복되게
        nr = row + dr[new_d]
        nc = col + dc[new_d]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0:
                robot(nr, nc, new_d)
                return # 보냈으면 끝냄



N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

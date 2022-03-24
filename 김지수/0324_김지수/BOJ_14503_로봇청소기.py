
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1] # 북동남서 0 1 2 3


def robot(row, col, direction):
    global result
    if arr[row][col] == 0:
        arr[row][col] = -1
        result += 1 # 청소
    for _ in range(4):
        new_d = (direction + 3) % 4 # 왼쪽으로 돌기
        nr = row + dr[new_d]
        nc = col + dc[new_d]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                robot(nr, nc, new_d)
                return # 보냈으면 끝냄
        direction = new_d # 바뀐 방향에서 왼쪽으로 가야하니까 direction 재정의
    # 네 군데 돌아봤는데 다 청소할 데가 없어서 return이 안 되었으면?
    temp_d = (direction + 2) % 4 # 뒤로
    new_r = row + dr[temp_d]
    new_c = col + dc[temp_d]
    if 0 <= new_r < N and 0 <= new_c < M:
        if arr[new_r][new_c] != 1:
            robot(new_r, new_c, direction)



N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
robot(r, c, d)
print(result)


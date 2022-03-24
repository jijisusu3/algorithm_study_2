import sys; sys.stdin = open('14503.txt', 'r')
from collections import deque

# 계속 수정해도 오답.... ㅠㅠ 벽 느껴진다...

N, M = map(int, input().split())
r, c, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

check = [[0]*M for _ in range(N)]
Q = deque()
Q.append((r, c, direction))

arr[r][c] = 1
check[r][c] = 1
result = 1

while Q:
    r, c, direction = Q.popleft()

    now_direction = direction
    turn_time = 0  # 회전횟수(4가 되면 후진)

    for i in range(4):
        now_direction -= 1  # 왼쪽 방향으로 회전
        if now_direction < 0:
            now_direction = 3

        nr = r + dr[now_direction]
        nc = c + dc[now_direction]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0 and check[nr][nc] == 0:  # 청소 가능한 부분
                check[nr][nc] = 1
                Q.append((nr, nc, now_direction))
                result += 1
                turn_time = 0
                break

            else:
                turn_time += 1
                if turn_time == 4:
                    nr = r - dr[now_direction]
                    nc = c - dc[now_direction]

                    if arr[nr][nc] == 0:
                        Q.append((nr, nc, now_direction))
                        break

                    elif arr[nr][nc] == 1:
                        break

                else:
                    continue
            arr[nr][nc] = 1
            result += 1

print(result)
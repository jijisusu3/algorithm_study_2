import sys; sys.stdin = open('2636.txt', 'r')
from collections import deque
# 아이디어
# (0, 0)의 좌표를 추가하고, bfs를 활용하여 우하좌상 이동했을 때, 1을 만나면 해당 부분들을 0으로 바꾸고, time += 1
# 치즈의 개수를 구하는 함수 생성
# 전체가 0이 되면 그 전에 저장된 치즈의 개수들 출력
# time 출력
# 다른사람 풀이 참고.... ㅠㅠ

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0:
                    if arr[nr][nc] == 1:
                        arr[nr][nc] = 0
                        visited[nr][nc] = 1
                        continue  # 아래 조건문 실행 x

                    if arr[nr][nc] == 0:
                        visited[nr][nc] = 1
                        Q.append((nr, nc))


def cheese():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
result_cheese = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]



# cheese가 0보다 많을 때, bfs 진행
# 이 부분 생각 못함...
while True:
    val = cheese()
    if val > 0:
        bfs(0, 0)
        time += 1
        result_cheese = val

    elif val == 0:
        break

print(time)
print(result_cheese)




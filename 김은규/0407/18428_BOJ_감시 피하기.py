# 아이디어
# 모든 x 좌표에 장애물 설치해보며 감시를 피할 수 있는지 탐색한다
# X를 O로 변경 후 개수 + 1 -> 3 이 됐을 때 T 위치에서 탐색
# X 를 O 로 바꿔주는 백트래킹 함수 생성
# T 위치에서 S 찾는 bfs 함수 생성


from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
arr = [list(input().split()) for _ in range(N)]

check = False

def bfs():
    teacher = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'T':
                teacher.append((i, j))

    while teacher:
        r, c = teacher.popleft()
        for k in range(4):
            temp_x, temp_y = r, c
            while True:
                nr = temp_x + dr[k]
                nc = temp_y + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 'S':
                        return False

                    elif arr[nr][nc] == 'O':
                        break

                    temp_x, temp_y = nr, nc
                else:
                    break
    return True

def perm(k):
    global check
    if k == 3:
        if bfs():
            check = True
        return

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                perm(k + 1)
                arr[i][j] = 'X'

perm(0)
if check:
    print('YES')
else:
    print('NO')





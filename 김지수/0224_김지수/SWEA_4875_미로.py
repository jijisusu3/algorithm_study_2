import sys;

sys.stdin = open('4875.txt')

dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]


def find(row, col, n):  # 시작 row, col, 크기N
    global success
    for i in range(4):
        if 0 <= (row + dr[i]) < n and 0 <= (col + dc[i]) < n:
            if maze[row + dr[i]][col + dc[i]] == '0':
                maze[row + dr[i]][col + dc[i]] = 'x'
                find(row + dr[i], col + dc[i], n)
                maze[row + dr[i]][col + dc[i]] = '0' # 원본 훼손 방지
            if maze[row + dr[i]][col + dc[i]] == '3':
                success = 1
                return


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    # 출발점(2) 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                start_r = r
                start_c = c
    success = 0
    find(start_r, start_c, N)
    if success == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    print(maze)

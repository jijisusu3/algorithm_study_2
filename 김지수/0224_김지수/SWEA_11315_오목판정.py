import sys; sys.stdin = open('11315.txt')

TC = int(input())
dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, -1, 1]

for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = False
    for r in range(N):
        for c in range(N):
            for i in range(8):
                if arr[r][c] == 'o':
                    cnt = 0
                    for j in range(1, 5):
                        nr = r + dr[i] * j
                        nc = c + dc[i] * j
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                cnt += 1
                    if cnt == 4:
                        result = True
    if result:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

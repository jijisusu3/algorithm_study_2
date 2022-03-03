# 시간초과.... 그러나 이정도면 만족...

import sys

M, N = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

good_tomato = []
unready = 0

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            good_tomato.append([r, c])
        elif arr[r][c] == 0:
            unready += 1

if unready == 0:
    print(0)

else:
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]  # 상하좌우

    cnt = 0
    change = 0
    while good_tomato and change < unready:
        how_many = len(good_tomato)
        for _ in range(how_many):
            tr = good_tomato[0][0]
            tc = good_tomato[0][1]
            good_tomato.pop(0)
            for i in range(4):
                nr = tr + dr[i]
                nc = tc + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = 1
                        change += 1
                        good_tomato.append([nr, nc])
        cnt += 1

    if change < unready:
        print(-1)
    else:
        print(cnt)




# 가로세로 합
import sys; sys.stdin = open('10593.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, 1, -1]

    result = 0
    for r in range(N):
        sum_v = 0
        for c in range(N):
            sum_v = arr[r][c]
            for i in range(4):
                nr, nc = r, c
                while 0 <= nr + dr[i] < N and 0 <= nc + dc[i] < N:
                    nr, nc = nr + dr[i], nc + dc[i]
                    sum_v += arr[nr][nc]


            if sum_v > result:
                result = sum_v

    print(f'#{tc} {result}')

#========================================================================\
# 대각 최대합

import sys; sys.stdin = open('11010.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, -1, 1, 1]  # 상하좌우
    dc = [-1, 1, 1, -1]

    result = 0
    for r in range(N):
        sum_v = 0
        for c in range(N):
            sum_v = arr[r][c]
            for i in range(4):
                nr, nc = r, c
                while 0 <= nr + dr[i] < N and 0 <= nc + dc[i] < N:
                    nr, nc = nr + dr[i], nc + dc[i]
                    sum_v += arr[nr][nc]


            if sum_v > result:
                result = sum_v

    print(f'#{tc} {result}')

#==========================================================================
# 사각영역들의 합
import sys; sys.stdin = open('11012.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for i in range(N)]




    '''
    R, C, S = map(int, input().split())
    result = 0
    for i in range(M):
        sum_v = 0
        for j in range(S):
            for k in range(S):
                sum_v += arr[R+j][C+k]

        result += sum_v

    print(f'#{tc} {result}')
    '''

#=====================================================================
# 폭격작전

import sys; sys.stdin = open('10989.txt', 'r')

T = int(input())
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
R, C, B = map(int, input().split())

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, 1, -1]

result = 0
for i in range(M):
    sum_v = 0
    for i in range(B):
        sum_v = arr[R][C]
        for i in range(4):
            nr, nc = R, C
            while 0 <= nr + dr[i] < N and 0 <= nc + dc[i] < N:
                nr, nc = nr + dr[i], nc + dc[i]
                sum_v += arr[nr][nc]

    result += sum_v

print(result)

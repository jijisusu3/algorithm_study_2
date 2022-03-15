# 11315_오목판정

import sys; sys.stdin = open('11315.txt')

def check(arr, N):
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    cnt = 0
                    r = i
                    c = j
                    while 0 <= r <= N - 1 and 0 <= c <= N - 1 and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                    if cnt >= 5:
                        return 'YES'

    return 'NO'


T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    arr = [input() for _ in range(N)]

    print('#{} {}'.format(tc, check(arr, N)))


# 3499_퍼펙트셔플

import sys; sys.stdin = open('3499.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())

    arr_a = []
    for i in range(len(arr)//2):
        arr_a.append(arr.pop(0))

    if len(arr) != len(arr_a):
        arr_a.append(arr.pop(0))

    result = []
    while len(arr) > 0:
        result.append(arr_a.pop(0))
        result.append(arr.pop(0))
    if len(arr_a) != 0:
        result.append(arr_a.pop())

    print('#{}'.format(tc), end=' ')
    for i in result:
        print(i, end=' ')
    print()


# 2805_농작물수확

import sys; sys.stdin = open('2805.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    cnt = 0
    for i in range(N//2 + 1):
        for j in range(N//2 - i, N//2 + i + 1):
            cnt += arr[i][j]
            if i != N//2:
                cnt += arr[N - i - 1][j]

    print('#{} {}'.format(tc, cnt))
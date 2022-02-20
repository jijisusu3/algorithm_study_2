import sys; sys.stdin = open('2001.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_max = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_fly = 0
            for k in range(M):
                for t in range(M):
                    sum_fly += arr[i + k][j + t]
            if sum_max < sum_fly:
                sum_max = sum_fly

    print('#{} {}'.format(tc, sum_max))

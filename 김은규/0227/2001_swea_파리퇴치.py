import sys; sys.stdin = open('2001.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(M):
                for m in range(M):
                    result += arr[i+k][j+m]

            if result > max_v:
                max_v = result

    print(f'#{tc} {max_v}')
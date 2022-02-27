import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 좌 우 상 하 대각 1, 2, 3, 4
    max_num = 0
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(M):
                for n in range(M):
                    ni = i + k
                    nj = j + n
                    if not 0 <= ni < N:
                        break
                    elif not 0 <= nj < N:
                        break
                    else:
                        total += arr[ni][nj]
            if max_num < total:
                max_num = total
    print(f"#{test_case} {max_num}")
import sys
sys.stdin = open('1979.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+2))
    arr = [[0]*(N+3)] + arr
    pattern = [0] + [1]*K + [0]
    cnt = 0
    for i in range(N+2):
        for j in range(N-K+2):
            for k in range(K+2):
                if arr[i][j+k] != pattern[k]:
                    break
            else:
                cnt += 1
    for j in range(N+2):
        for i in range(N-K+2):
            for k in range(K+2):
                if arr[i+k][j] != pattern[k]:
                    break
            else:
                cnt += 1
    print(f"#{test_case} {cnt}")

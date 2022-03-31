import sys; sys.stdin = open('123.txt')

# N 벌통크기 M 선택가능한 벌통개수 C 채취할 수 있는 최대 양
T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N - 1):
        for j in range(N):
            if j + M - 1 < N:
                arr_1 = []
                for k in range(M):
                    arr_1.append(arr[i][j + k])
                    arr_2 = []
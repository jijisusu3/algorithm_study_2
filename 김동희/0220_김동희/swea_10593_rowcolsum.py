import sys; sys.stdin = open('swea_10593_rowcolsum.txt')
TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    if N == 1:
        ans = int(input())
        print(f'#{tc} {ans}')
    # elif N == 2:

    else:
        arr = [list(map(int,input().split())) for _ in range(N)]
        ans = [[0]*N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                for i in range(N):
                    ans[r][c] += arr[r][i]
                    ans[r][c] += arr[i][c]
                ans[r][c] -= arr[r][c]

        max_v = 0
        for i in ans:
            if max_v < max(i):
                max_v = max(i)

        print(f'#{tc} {max_v}')

    # ans[r][c]
    # if r == 0 and c == 0:
    #     for i in range(N):
    #         ans[r][c] += arr[r][i]
    #         ans[r][c] += arr[i][c]
    #     ans[r][c] += arr[r][c]
    #
    # if r == 0 and c == 1:
    #     for i in range(N):
    #         ans[r][c] += arr[r][i]
    #         ans[r][c] += arr[i][c]
    #     ans[r][c] += arr[r][c]
    #
    # if r == 0 and c == 2 :
    #     for i in range(N):
    #         ans[r][c] += arr[r][i]
    #         ans[r][c] += arr[i][c]
    #     ans[r][c] += arr[r][c]
    #




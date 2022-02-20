import sys
sys.stdin = open("11014_농작물 수확.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    crops_total = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        board.append(arr)
        for j in range(N):
            crops_total += arr[j]
    min_value = int(1e9)
    # 좌표
    for i in range(1, N):
        for j in range(1, N):
            row, col = i, j # 구획 좌표
            sum1 = 0
            for r in range(row):
                for c in range(col):
                    sum1 += board[r][c]
                sum2 = 0
                for c2 in range(col):
                    for r2 in range(N-1, row-1, -1):
                        sum2 += board[r2][c2]
            sum3 = crops_total - sum1 - sum2
            min_value = min(min_value, max(sum1, sum2, sum3)-min(sum1, sum2, sum3))
    print(f"#{t}", min_value)
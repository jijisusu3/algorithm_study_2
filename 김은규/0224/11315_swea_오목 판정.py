import sys; sys.stdin = open('11315.txt', 'r')

# 행 우선 순회하다가 'o' 나오면 우, 하, 우하, 좌하
def solve(arr):
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    r, c = i, j
                    # 해당 방향으로 계속 이동하며 개수 세기
                    # r,c 범위 안에 있으면 돌 존재하면 반복
                    cnt = 0  # 연속적으로 놓인 돌의 개수

                    while 0 <= r < N and 0 <= c < N and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                        if cnt >= 5: return 'YES'

    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = solve(arr)
    print(f'#{tc} {result}')
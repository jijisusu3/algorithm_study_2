import sys; sys.stdin = open('swea_11010_dia_sum.txt')

TC =int(input())
# 우상 우하 좌상 좌하
dr = [-1,1,-1,1]
dc = [1,1,-1,-1]
for tc in range(1,TC+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_r = 0
    for r in range(N):
        for c in range(N):
            result = 0
            result += arr[r][c]
            for i in range(4):
                for j in range(1,N-1):
                    r += dr[i]* j
                    c += dc[i]* j
                    if r <0 or c<0 or r>N-1 or c>N-1 :
                        r -= dr[i] * j
                        c -= dc[i] * j
                    else:
                        result += arr[r][c]
                        r -= dr[i] * j
                        c -= dc[i] * j
            if result > max_r:
                max_r = result
    print(f'#{tc} {max_r}')









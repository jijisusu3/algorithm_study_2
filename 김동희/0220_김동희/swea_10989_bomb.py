import sys; sys.stdin = open('swea_10989_bomb.txt')

TC =int(input())
# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    zrr = [[0]*N for _ in range(N)]
    for _ in range(M):
        r ,c, a = map(int,input().split())
        r1, c1 = r, c
        zrr[r][c] = arr[r][c]
        for j in range(4):
            for i in range(a):
                r1 += dr[j]
                c1 += dc[j]
                if r1 <0 or c1<0 or r1>N-1 or c1>N-1 or zrr[r1][c1]!=0:
                    pass
                else:
                    zrr[r1][c1] = arr[r1][c1]
            r1 = r
            c1 = c
    #합
    result = 0
    for a in range(N):
        for b in range(N):
            result += zrr[a][b]
    print(f'#{tc} {result}')








import sys; sys.stdin = open('swea_11012_sq_sum.txt')

TC =int(input())
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    zrr = [[0]*N for _ in range(N)]
    for _ in range(M):
        r ,c, a = map(int,input().split())
        for r1 in range(r,r+a):
            for c1 in range(c,c+a):
                if r1<0 or c1<0 or r1>N-1 or c1>N-1 or zrr[r1][c1]!=0:
                    continue
                else:
                    zrr[r1][c1] = arr[r1][c1]
    result = 0
    for i in range(N):
        for j in range(N):
            result += zrr[i][j]
    print(f'#{tc} {result}')
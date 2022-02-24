import sys; sys.stdin=open('swea_오목.txt')

#오목 체크 함수
def check_omoc(N):
    for r in range(N):
        for c in range(N):
            for k in range(8):
                if arr[r][c] == 'o':
                    cnt = 1
                    for i in range(1,5):
                        nr = r + dr[k]*i
                        nc = c + dc[k]*i
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] =='o':
                                cnt += 1
                    if cnt == 5:
                        return 'YES'
    else:
        return 'NO'


TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 우 하 좌 상 우하, 좌하, 좌상, 우상
    dr = [0,1,0,-1,1,1,-1,-1]
    dc = [1,0,-1,0,1,-1,-1,1]
    print(f'#{tc}',check_omoc(N))


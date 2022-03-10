import sys;
# sys.stdin=open('boj_1012_유기농배추.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(r,c):
    arr[r][c] = 0
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0<=nr<R and 0<=nc<C and arr[nr][nc]:
            arr[nr][nc] = 0
            dfs(nr,nc)

# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

TC = int(input())
for tc in range(TC):
    R,C,N = map(int,input().split())
    arr = [[0]*C for _ in range(R)]
    # visited = [[0]*R for _ in range(C)]
    cnt = 0
    for n in range(N):
        r,c = map(int,input().split())
        arr[r][c] = 1

    for r in range(R):
        for c in range(C):
            if arr[r][c]:
                cnt += 1
                dfs(r,c)
    print(cnt)
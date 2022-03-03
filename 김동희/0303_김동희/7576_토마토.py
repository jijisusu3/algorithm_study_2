import sys; sys.stdin=open('7576_토마토.txt')


#우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def bfs(lst):
    queue = lst
    while queue:
        r1,c1 = queue.pop(0)
        for d in range(4):
            nr = r1+dr[d]
            nc = c1+dc[d]
            if 0<= nr <N and 0<= nc <M and not arr[nr][nc]:
                arr[nr][nc] = 1 # 그냥 0으로 바꾸기
                queue.append((nr,nc))

    return


N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
visit = [[0]*N for _ in range(M)]
lst = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            lst.append((r,c))




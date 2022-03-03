import sys; sys.stdin=open('2667_단지번호_dfs.txt')

#우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def bfs(r,c):
    cnt = 1
    queue = [(r,c)]
    arr[r][c] = 0 # 그냥 0으로

    while queue:
        r,c = queue.pop(0)
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if 0<= nr <N and 0<= nc <N and arr[nr][nc]:
                arr[nr][nc] = 0 # 그냥 0으로 바꾸기
                queue.append((nr,nc))
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
# visit = [[0]*N for _ in range(N)]
result = []
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            result.append(bfs(r,c))
print(len(result))
for i in sorted(result):
    print(i)



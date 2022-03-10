import sys
# sys.stdin = open('boj_10026_적록색약.txt')
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(r, c):
    visited[r][c]=1
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<N and arr[r][c]==arr[nr][nc] and visited[nr][nc]==0:
            dfs(nr, nc)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]
# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
cnt1 = 0

for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            cnt1+=1
            dfs(i, j)

for i in range(N):
    for j in range(N):
        if arr[i][j]=='R':
            arr[i][j]='G'

cnt2 = 0
visited = [[0]*(N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            cnt2+=1
            dfs(i, j)

print(cnt1,cnt2)


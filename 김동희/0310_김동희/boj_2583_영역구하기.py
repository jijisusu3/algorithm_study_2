import sys
sys.stdin = open('boj_2583_영역구하기.txt')
input = sys.stdin.readline
#우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

#arr = 세로/가로/작은arr 갯수
M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
# visited = [[0]*N for _ in range(M)]
for k in range(K):
    l_x, l_y, r_x, r_y = map(int,input().split())
    x1, y1 = M-1-l_y, l_x
    x2, y2 = N-2-r_y, r_x-1

    for r in range(x2,x1+1):
        for c in range(y1,y2+1):
            arr[r][c] = 1

# print(arr)

def bfs(r,c):
    cnt = 1
    queue = [(r,c)]
    arr[r][c] = 1
    while queue:
        r, c = queue.pop()
        for d in range(4):
            nr , nc = r + dr[d], c + dc[d]
            if 0<= nr < M and 0 <= nc <N and not arr[nr][nc] :
                queue.append((nr,nc))
                arr[nr][nc] = 1
                cnt += 1
    return cnt

count = 0
result = []
for r in range(M):
    for c in range(N):
        if not arr[r][c]:
            result.append(bfs(r,c))
            count += 1

print(count)
print(*sorted(result))
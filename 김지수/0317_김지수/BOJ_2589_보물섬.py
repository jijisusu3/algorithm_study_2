from collections import deque

N, M = map(int, input().split())
island = [list(input()) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(row, col):
    cnt = 0
    Q = deque()
    Q. append((row, col))
    visited[row][col] = 1 # 0과 다르게 하려고 출발지에서는 0시간인데 여기서 1로 해놨으니,
    while Q:
        sr, sc = Q.popleft()
        for i in range(4):
            nr = sr + d[i][0]
            nc = sc + d[i][1]
            if 0 <= nr < N and 0 <= nc < N:
                if island[nr][nc] == 'L' and visited[nr][nc] == 0:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1 # 몇시간 왔나 세기
                    if visited[nr][nc] > cnt:
                        cnt = visited[nr][nc]
    return cnt - 1 # 여기서 1을 빼줘야 온 시간이 계산됨


result = []
for r in range(N):
    for c in range(M):
        if island[r][c] == 'L':
            visited = [[0] * M for _ in range(N)] # 매번 출발할 때마다 초기화~
            result.append(bfs(r, c))
print(max(result))
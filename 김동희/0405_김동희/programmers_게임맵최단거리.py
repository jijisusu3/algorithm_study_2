def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visit = [[0]*M for _ in range(N)]
    def bfs(sr,sc):
        Q = [(sr,sc)]
        visit[sr][sc] = 1
        while Q:
            r, c = Q.pop(0)
            if r == N-1 and c == M -1:
                return visit[r][c]

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0<=nr<N and 0<=nc<M and not visit[nr][nc] and maps[nr][nc]:
                    visit[nr][nc] = visit[r][c]+ 1
                    Q.append((nr,nc))
        return -1
    answer = bfs(0,0)
    return answer

ans = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
print(ans)
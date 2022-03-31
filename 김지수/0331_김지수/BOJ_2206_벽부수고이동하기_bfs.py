from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs는 최소조건을 달 필요가 없음. 신기


def bfs(row, col, wall_cnt, visited, arr):
    queue = deque()
    queue.append((row, col, wall_cnt))
    visited[row][col][wall_cnt] = 1

    while queue:
        r, c, wall_cnt = queue.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][wall_cnt]

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if nr <= -1 or nr >= N or nc <= -1 or nc >= M:
                continue

            if arr[nr][nc] == 0 and visited[nr][nc][wall_cnt] == 0:
                queue.append((nr, nc, wall_cnt))
                visited[nr][nc][wall_cnt] = visited[r][c][wall_cnt] + 1

            if arr[nr][nc] == 1 and wall_cnt == 0:
                queue.append((nr, nc, wall_cnt + 1))
                visited[nr][nc][wall_cnt + 1] = visited[r][c][wall_cnt] + 1

    return -1


print(bfs(0, 0, 0, visited, arr))
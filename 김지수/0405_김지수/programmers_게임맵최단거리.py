from collections import deque


def solution(maps):
    N = len(maps)  # 행 row
    M = len(maps[0])  # 열 col
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((0, 0, 1))
    visited[0][0] = 1
    while Q:
        row, col, now_cnt = Q.popleft()
        if row == N - 1 and col == M -1:
            return now_cnt

        for nr, nc in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col -1)]:
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and maps[nr][nc] == 1:
                    visited[nr][nc] = 1
                    Q.append((nr, nc, now_cnt + 1))

    return -1


arr = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(arr))
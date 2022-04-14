from collections import deque
import sys

d = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
H, W = map(int, input().split())  # 가로세로
arr = [list(sys.stdin.readline().rstrip()) for i in range(H)]
visited = [[0] * W for _ in range(H)]
Q = deque()

for r in range(H):
    for c in range(W):
        if arr[r][c] == '.':
            arr[r][c] = 0
            Q.append((r, c))
        else:
            arr[r][c] = int(arr[r][c])

result = 0

while len(Q):
    row, col = Q.popleft()
    for i in range(8):
        nr, nc = row + d[i][0], col + d[i][1]
        if 0 <= nr < H and 0 <= nc < W:
            if arr[nr][nc] != 0:
                arr[nr][nc] -= 1
                if arr[nr][nc] == 0:
                    visited[nr][nc] = visited[row][col] + 1
                    result = max(result, visited[nr][nc])
                    Q.append((nr, nc))
print(result)
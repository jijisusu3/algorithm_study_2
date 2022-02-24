import sys; sys.stdin = open('11610.txt')


def DFS(a, b):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < V and 0 <= y < V and not visited[x][y]:
            if not maze[x][y]:
                visited[x][y] = 1
                if DFS(x, y):
                    return 1
            elif maze[x][y] == 3:
                return 1

T = int(input())
for tc in range(1, T + 1):
    V = int(input())
    maze = [list(map(int, input())) for _ in range(V)]
    visited = [[0] * (V) for _ in range(V)]
    
    result = 0
    for i in range(V):
        for j in range(V):
            if maze[i][j] == 2:
                if DFS(i, j):
                    result = 1
                else:
                    result = 0

    print('#{} {}'.format(tc, result))


# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# N = int(input())
# maze = [input() for _ in range(N)]
# sr = sc = 0
# for i in range(N):
#     for j in range(N):
#         if maze[i][j] == '2':
#             sr, sc = i, j
#         if maze[i][j] == '3':
#             er, ec = i, j

# def DFS(r, c):
#     # 현재 위치를 방문하고
#     visited[r][c] = 1
#     # 인접 정점을 찾는다. 네 방향의 좌표를 생성
#     for i in range(4):
#         nr, nc = r + dr[i], c + dc[i]
#         # 제외해야할 경우 (경계체크)
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             continue
#         # 길인지, 방문했는지 체크
#         if maze[nr][nc] == '1' or visited[nr][nc] == 1:
#             continue
#         DFS(nr, nc)


# visited = [[0] * N for _ in range(N)]
# DFS(sr, sc)
# print(visited[er][ec])
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1] # 상하좌우


def bfs():
    fire = deque()
    people = deque()
    for r in range(H):
        for c in range(W):
            if building[r][c] == '*':
                fire.append((r, c))
                visited[r][c] = 1
            elif building[r][c] == '@':
                people.append((r, c))
                building[r][c] = 0

    while people:
        temp_1 = deque()
        while people:
            row, col = people.popleft()
            if (row == H - 1 or col == W - 1 or row == 0 or col == 0) and building[row][col] != '*':
                return building[row][col]
            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if building[nr][nc] == '.' and visited[row][col] == 0:
                        building[nr][nc] = building[row][col] + 1
                        temp_1.append((nr, nc))
        people = temp_1

        temp_2 = deque()
        while fire:
            row, col = fire.popleft()
            # 불 번짐
            for x in range(4):
                new_r, new_c = row + dr[x], col + dc[x]
                if 0 <= new_r < H and 0 <= new_c < W:
                    if visited[new_r][new_c] == 0 and building[new_r][new_c] != '#':
                        building[new_r][new_c] = '*'
                        visited[new_r][new_c] = 1
                        temp_2.append((new_r, new_c))
        fire = temp_2


TC = int(input())
for _ in range(TC):
    W, H = map(int, input().split())
    building = [list(input()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    result = bfs()

    if result is not None:
        print(result + 1)
    else:
        print('IMPOSSIBLE')
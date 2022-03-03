# 아직 다 못풀었습니다....

def bfs():
    while lst:
        i, j = lst.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    arr[ni][nj] = 1
                    visited[ni][nj] = visited[i][j] + 1  # 하루에 1씩 증가하고, 마지막에 최대 일수 구하기 위해서
                    lst.append([ni, nj])

M, N = map(int, input().split())  # 가로 M, 세로 N
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
lst = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            lst.append([i,j])

bfs()






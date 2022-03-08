# 아이디어
# visited 배열과 arr 배열을 비교하여 둘 다 0인 경우만 진행되도록 설정
# 동시다발적으로 진행하지 않고 풀기
# 시간초과.......

def bfs(arr, visited):
    while lst:
        i, j = lst.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    arr[ni][nj] = 1
                    visited[ni][nj] = visited[i][j] + 1  # 하루에 1씩 증가하고, 마지막에 최대 일수 구하기 위해서
                    lst.append([ni, nj])

    for k in range(N):
        for m in range(M):
            if arr[k][m] == 0:
                return -1

    max_v = -2
    for z in range(N):
        for x in range(M):
            if visited[z][x] > max_v:
                max_v = visited[z][x]

    return max_v

M, N = map(int, input().split())  # 가로 M, 세로 N
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
lst = []


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            lst.append([i,j])

print(bfs(arr, visited))








N = int(input())
M = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
start = 0
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1
result = 0


def bfs(visit):
    visited[visit] = 1
    global result
    for x in range(1, N + 1):
        if arr[visit][x] == 1 and visited[x] == 0:
            result += 1
            bfs(x)
    return


bfs(1)
print(result)

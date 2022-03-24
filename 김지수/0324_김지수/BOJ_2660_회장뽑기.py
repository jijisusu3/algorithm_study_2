from collections import deque


def bfs(start):
    visited = [-1] * (N + 1)
    Q = deque()
    Q.append(start)
    visited[start] = 0
    while Q:
        x = Q.popleft()
        for f in lst[x]:
            if visited[f] == -1:
                visited[f] = visited[x] + 1
                Q.append(f)
    result[start] = max(visited)
    return


N = int(input())
lst = [[] for _ in range(N + 1)]
result = [[0] for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    lst[a].append(b)
    lst[b].append(a)

for i in range(1, N + 1):
    bfs(i)

a = min(result[1:])
xx = []
for i in range(1, N + 1):
    if result[i] == a:
        xx.append(i)
print(a, len(xx))
print(*xx)

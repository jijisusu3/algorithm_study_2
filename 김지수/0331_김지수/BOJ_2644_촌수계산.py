from collections import deque


def bfs(X):
    Q = deque()
    Q.append(X)
    while Q:
        start = Q.popleft()
        for i in lst[start]:
            if visited[i] == 0:
                visited[i] = visited[start] + 1
                Q.append(i)


N = int(input())  # 전체 사람 수
a, b = map(int, input().split()) # 이 둘의 촌수를 구해야함
lst = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

bfs(a)

if visited[b] > 0:
    print(visited[b])
else:
    print(-1)
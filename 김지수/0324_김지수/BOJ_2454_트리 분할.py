
def dfs(start, k, y):
    if k == len(y):
        if node[start] > 1:
            return 0
        else:
            return 1
    if visited[start] == 0:
        visited[start] = 1
        k += 1
        for x in node[start]:
            a = dfs(x, k, y)
            if a == 1:


N, K = map(int, input().split())
node = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N+1)]
Y = ''
for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

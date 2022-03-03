import sys; sys.stdin=open('2606_바이러스_dfs.txt')
# import sys
n = int(input())
m = int(input())
graph = [[]  for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

cnt = 0
visited = [0] * (n + 1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if not visited[i] :
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)
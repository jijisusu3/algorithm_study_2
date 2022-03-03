import sys; sys.stdin=open('2606_바이러스_dfs.txt')
# import sys
from collections import deque

def bfs(s):
    queue = deque([s])
    while queue:
        node = queue.popleft()
        visited[node] = 1
        queue.extend(graph[node])
    return sum(visited)-1


N = int(input())
G = int(input())
graph = [[] for _ in range(N+1)]
for g in range(G):
    s, e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
visited = [0]*(N+1)
print(bfs(1))




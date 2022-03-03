import sys; sys.stdin = open('2606.txt')

def dfs(i):
    global cnt
    visited[i] = 1
    for j in graph[i]:
        if visited[j] == 0:
            dfs(j)
            cnt += 1

N = int(input())
T = int(input())
graph = [[] * N for _ in range(N + 1)]
for _ in range(T):
    a, b= map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (N + 1)

dfs(1)
print(cnt)
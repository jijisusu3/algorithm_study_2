import sys; sys.stdin = open('2606.txt', 'r')

Com = int(input())  # 정점수
E = int(input())  # 간선수
G = [[] for _ in range(Com+1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

visited = [0]*(Com + 1)  # 체크리스트
queue = []  # 큐 생성
queue.append(1)
visited[1] = 1
while queue:
    t = queue.pop(0)
    for i in G[t]:
        if not visited[i]:
            queue.append(i)
            visited[i] = 1

print(visited.count(1)-1)  # 1제외하기 위해서 -1


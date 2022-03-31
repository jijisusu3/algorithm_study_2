# 아이디어
# 무향그래프 만들고
# visit 을 체크하면서 찾는 번호로부터 얼마나 떨어져있는지 구한다
from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]  # 정점 수 + 1 만큼
for i in range(M):
    x, y = map(int, input().split())  # 무방향
    graph[x].append(y)
    graph[y].append(x)
    # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

visit = [0] * (N + 1)
q = deque()
q.append(a)
while q:
    s = q.popleft()
    for i in graph[s]:
        if visit[i] == 0:
            visit[i] = visit[s] + 1
            q.append(i)

if visit[b] > 0:
    print(visit[b])

else:
    print(-1)
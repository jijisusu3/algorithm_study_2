# 아이디어
# 데이터를 받아 그래프를 만든다
# 노드 개수 많은 사람이 회장 후보
# BFS 활용하여 다음 사람으로 넘어갈 때 visit +1 씩 해준다
# check 가장 많은 사람들이 회장 후보
# 점수는 노드 개수가 N - 1 일 경우 1점, 그 외에 하나씩 줄어들 때마다 1점 추가
# 근데 이러면 시작점이 어디냐에 따라서 visit 값이 달라지는데...

import sys; sys.stdin = open('2660.txt', 'r')
from collections import deque

def BFS(i, N):
    visit = [0] * (N + 1)
    q = deque()
    q.append(i)
    visit[i] = 1
    while q:
        s = q.popleft()
        for i in Graph[s]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = visit[s] + 1

    return

N = int(input())
Graph = [[] for _ in range(N+1)]
node = 0

while True:
    i, j = map(int, input().split())
    if i == -1 and j == -1:
        break
    Graph[i].append(j)
    Graph[j].append(i)

for i in range(1, N+1):
    BFS(i, N)

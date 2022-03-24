import sys; sys.stdin = open('123.txt')
from collections import deque

Q = deque()
def bfs(n):
    visit[n] = 1
    Q.append(n)
    while Q:
        x = Q.popleft()
        for i in arr[x]:
            if visit[i] == 0:
                Q.append[i]
                score[i] = score[x] + 1
                visit[i] = 1

N = int(input())
arr = [[] for _ in range(N + 1)]
while arr:
    a, b = map(int, input().split())
    if a == -1:
        break
    arr[a].append(b)
    arr[b].append(a)

runner = []
max_runner = 51
for i in range(1, N + 1):
    score = [0] * (N + 1)
    visit = [0] * (N + 1)
    bfs(i)
    a = 0
    for j in score:
        if j > a:
            a = j
    if a < max_runner:
        runner = [i]
        max_runner = a
    elif a == max_runner:
        runner.append(i)

print(max_runner, len(runner))
for i in runner:
    print(i, end = ' ')
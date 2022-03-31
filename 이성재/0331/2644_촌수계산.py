import sys; sys.stdin = open('123.txt')
from collections import deque

def bfs(a):
    q = deque()
    q.append(a)
    visit[a] = 1

    while q:
        x = q.pop()

        for i in arr[x]:
            if visit[i] == 0:
                visit[i] = 1
                rst[i] = rst[x] + 1
                q.append(i)

n = int(input())
A, B = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
cnt = 0
while cnt < m:
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    cnt += 1

visit = [0 for _ in range(n + 1)]
rst = [0 for _ in range(n + 1)]

bfs(A)
if rst[B] != 0:
    print(rst[B])
else:
    print(-1)
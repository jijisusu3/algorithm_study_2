from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(lst[x])
            break
        for now in (x-1, x+1, 2*x):
            if 0 <= now <= 100000 and lst[now] == 0:
                lst[now] = lst[x] + 1
                q.append(now)


N, K = map(int, input().split())
lst = [0]*100001
bfs()



import sys; sys.stdin = open('1697.txt')  # 틀림..
from collections import deque

n, k = map(int, input().split())
visit = [0 for _ in range(100001)]
Q = deque()
Q.append(n)
while Q:
    site = Q.popleft()
    if site == k:
        print(visit[k])
    for i in (site - 1, site + 1, site * 2):
        if 0 <= i < 100001 and visit[i] == 0:
            visit[i] = visit[site] + 1
            Q.append(i)
# ord로 A~Z 는 65~90
from collections import deque


def bfs(A):
    global count
    q = deque()
    q.append(65)
    while q:
        x = q.popleft()
        if x == A:
            count += lst[x]
            break
        for now in (x-1, x+1, 65, 90):
            if 65 <= now <= 90 and lst[now] == 0:
                lst[now] = lst[x] + 1
                q.append(now)


name = list("JAN")
start = 65
count = 0
while name:
    lst = [0] * 100
    a = name.pop(0)
    a = ord(a)
    bfs(a)

print(count)



# def dfs(s, A, cnt):
#     global lst
#     if s == A:
#         lst.append(cnt)
#         return
#     if visited[s] == 0 and s == 65:
#         visited[s] = 1
#         dfs(90, A, cnt + 1)
#         visited[s] = 0
#     elif visited[s] == 0 and s == 90:
#         visited[s] = 1
#         dfs(65, A, cnt + 1)
#         visited[s] = 0
#     for x in (s + 1, s - 1):
#         if visited[x] == 0 and 65 <= x < 91:
#             visited[x] = 1
#             dfs(x, A, cnt + 1)
#             visited[x] = 0
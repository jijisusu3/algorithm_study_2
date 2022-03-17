# 풀이 참조...
# 근데 if 문의 순서 상관이 없는 건가??

from collections import deque

n, k = map(int, input().split())
queue = deque([n])
visited = [0] * 100001
visited[n] = 1

while queue:
    a = queue.popleft()
    if a == k:
        print(visited[a] - 1)
        break

    if 2 * a <= 100000 and visited[2 * a] == 0:
        queue.append(2 * a)
        visited[2 * a] = visited[a] + 1

    if a + 1 <= 100000 and visited[a + 1] == 0:
        queue.append(a + 1)
        visited[a + 1] = visited[a] + 1

    if a - 1 >= 0 and visited[a - 1] == 0:
        queue.append(a - 1)
        visited[a - 1] = visited[a] + 1




import sys; sys.stdin=open('boj_17471_게리맨더링.txt')
from collections import deque

# 연결이 되었는가
def bfs_connect_check(area):
    visit = [0] * (N+1)
    q = deque()
    q.append(area[0])
    visit[area[0]] = 1
    total_people = 0
    cnt = 1
    while q:
        node = q.popleft()
        total_people += people[node]
        for v in node_arr[node]:
            if v in area and not visit[v]:
                visit[v] = 1
                cnt += 1
                q.append(v)
    if cnt == len(area):
        return total_people
    else:
        return 0


def dfs(k, s):
    global result
    if k == s:
        area1, area2 = [], []

        for i in range(1, N+1):
            if visit[i]:
                area1.append(i)
            else:
                area2.append(i)
        # 연결이 되었는가
        x = bfs_connect_check(area1)
        y = bfs_connect_check(area2)
        if x and y:
            result = min(result, abs(x-y))
        return

    for i in range(1, N+1):
        if not visit[i]:
            visit[i] = 1
            dfs(k+1, s)
            visit[i] = 0

# 테스트케이스 연결해봄.
T = int(input())
for t in range(1,1+T):
    #사람수.
    N = int(input())
    people = [0]+ list(map(int,input().split()))
    node_arr = [[] for _ in range(N+1)]
    for n in range(N):
        temp = list(map(int,input().split()))
        node_arr[n+1] = temp[1:]
    print('total_people :',people)
    print('node_arr :',node_arr)
    result = int(1e9)
    # 두 구역으로 나누는 경우의 수.
    # 각 구역끼리 인접하는 가.

    # 구역을 나누는 경우의 수
    for i in range(1, N // 2 + 1):
        visit = [0]*(N+1)
        dfs(0, i)

    if result == int(1e9):
        print(f'{t}번 result (없음을 의미) :',-1)
    else:
        print(f'{t}번 result :',result)




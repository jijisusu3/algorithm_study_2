import sys; sys.stdin = open('123.txt')

N, M, k = map(int, input().split())
friend_fee = [0] + list(map(int, input().split()))

arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 방문표시 and 친구관계 담기
visit = [0] * (N + 1)
relation = []

# dfs로 친구무리
def dfs(a, save):
    for i in arr[a]:
        if visit[i] == 0:
            visit[i] = 1
            save.append(i)
            dfs(i, save)

# dfs 돌려주기 => 친구무리별로 저장
for i in range(1, N + 1):
    if visit[i] == 0:
        save = [i]
        visit[i] = 1
        dfs(i, save)
        relation.append(save)

# 친구무리 중 낮은금액 더해주기
rst = 0
for i in relation:
    fee = 9999999999
    for j in i:
        if fee > friend_fee[j]:
            fee = friend_fee[j]
    rst += fee

if rst <= k:
    print(rst)
else:
    print('Oh no')
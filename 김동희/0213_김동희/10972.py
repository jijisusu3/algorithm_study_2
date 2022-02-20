N = int(input())                             # 4

l =  [i for i in range(1,N+1)]               # 1 2 3 4 
visited = [0 for _ in range(len(l))]         # [0,0,0,0]
answer = []                                  # []

def dfs(cnt, list):                          # 0 , []
    if cnt == len(l):
        answer.append(list[:])
        return

    for i, val in enumerate(l):              # 0, 1
        # 만약 방문했다면 건너 뛰기(순열을 위함)
        if visited[i] == 1:
            continue
        # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)                     # [1]
        visited[i] = 1                       # [1,0,0,0]

        dfs(cnt+1, list)                     # 2 , [2] -> 1,2 : 
        # 방금 전 list에 추가한 값과 방문 한 것을 되돌려주기
        list.pop()
        visited[i] = 0


dfs(0, [])
# print(answer)
arr = list(map(int, input().split()))
for k, v in enumerate(answer):
    
    if arr == v:
        if k == len(answer)-1:
            print(-1)
            break
        for a in answer[k+1]:
            print(a, end=" ")
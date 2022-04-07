import sys; sys.stdin = open('123.txt')

# 가능한 7개 찾고, 7개 붙어 있는지 따로 확인한 이유
# 한곳 잡고 7칸 이동해서 조건 맞는지 확인하려 했지만 첫칸부터 다 찾아야하고 중복 떨궈줘야되서 사실상 다 찾아야함

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 7개가 서로 연결되어 있는지 확인!
def check(s):
    global ctn    # ctn은 7명 붙어있는지 확인용
    x = s // 5
    y = s % 5
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if visit[nx][ny] == 0:
                if (nx * 5 + ny) in p:     # 다음숫자가 p에 있다면 방문표시 후 재귀
                    ctn += 1    # 연결된 숫자 갯수 새기
                    visit[nx][ny] = 1
                    check((nx * 5 + ny))

# cnt ==> 7명 뽑을 때까지, idx ==> 사용할 숫자, cnt_y ==> 임도연파 수
# p[] 에 7개가 들어가면 check로 검증
def dfs(cnt, idx, cnt_y):
    global ans, visit, ctn
    
    if cnt_y > 3 or 25 - idx < 7 - cnt:  # 임도연파 수가 더 많아지거나 탐색해야 할 숫자가 남은 선택 수보다 적어지면 가지치기
        return
        
    if cnt == 7:
        ctn = 1  # 매번 초기화(ctn, visit)
        visit = [[0] * 5 for _ in range(5)]
        nx, ny = p[0] // 5, p[0] % 5
        visit[nx][ny] = 1       # 시작위치 먼저 표시
        check(p[0])
        if ctn == 7:
            ans += 1 
        return
    
    x = idx // 5    # 처음에 for문 두개써서 싹다 보려고 하니 안 됌.. 칸이 5x5로 정해져 있어서 좌표를 변수 하나만 써서 정함!
    y = idx % 5     # idx == 1 이면 (0, 0) 2면 (0, 1) ...
    
    p.append(idx)
    if arr[x][y] == 'Y':         # 임도연파가 많아지면 가지치기 하는게 편하므로 임도연파 명수 기준으로
        dfs(cnt + 1, idx + 1, cnt_y + 1)
    else:
        dfs(cnt + 1, idx + 1, cnt_y)
    p.pop()
    dfs(cnt ,idx + 1, cnt_y)   # 인덱스 넘기기용
    
arr = [list(map(str, input())) for _ in range(5)]
visit = [[0] * 5 for _ in range(5)]
ans = 0
p = []

dfs(0, 0, 0)
print(ans)





# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def oo(i, j, cnt, cnt_y):
#     global rst

#     if cnt_y > 3:
#         return
#     if cnt == 7:
#         rst += 1
#         return

#     for a in range(4):
#         nx = i + dx[a]
#         ny = j + dy[a]
#         if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
#             if arr[nx][ny] == 'S':
#                 visited[nx][ny] = 1
#                 oo(nx, ny, cnt + 1, cnt_y)
#                 visited[nx][ny] = 0
#             elif arr[nx][ny] == 'Y':
#                 visited[nx][ny] = 1
#                 oo(nx, ny, cnt + 1, cnt_y + 1)
#                 visited[nx][ny] = 0

# arr = [list(map(str, input())) for _ in range(5)]

# rst = 0

# for i in range(5):
#     for j in range(5):
#         visited = [[0] * 5 for _ in range(5)]
#         visited[i][j] = 1
#         if arr[i][j] == 'S':
#             oo(i, j, 1, 0)
#         else:
#             oo(i, j, 1, 1)

# print(rst)
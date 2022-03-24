import sys; sys.stdin=open('boj_2636_치즈.txt')

'''
입력 :
세로 N, 가로 M, 최대 100
치즈가 없는칸 0, 치즈가 있는칸 1,
출력 : 모두 녹는 시간, 한시간전 남아있는 치즈수
풀이 : if 우하좌상이 0이면 visit = 1 bfs 탐색진행 
    / elif 1이면 0으로 바꿔 visit = 1 & cnt += 1 bfs 탐색진행 X  
    visit을 bfs탐색 시작할 때, 0으로 초기화. why? 0,0으로 시작할 것이기 때문.
결과1 : 반복 작업 수를 추출
결과 : 찾는 값이 없으면 그전의 1의 값을 추출 
'''
def BFS(sr, sc):
    q = [(sr, sc)]
    cnt = 0
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if nr<0 or nr>=N or nc<0 or nc>=M: continue;

            if not visit[nr][nc] and not arr[nr][nc]:
                q.append((nr,nc))
                visit[nr][nc] = 1

            elif not visit[nr][nc] and arr[nr][nc]:
                visit[nr][nc] = 1
                arr[nr][nc] = 0
                cnt += 1
    return cnt

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

#우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
t = -1
ans = count = 1

while count > 0:
    t += 1
    ans = count
    visit = [[0] * M for _ in range(N)]
    count = BFS(0,0)
print(t)
print(ans)




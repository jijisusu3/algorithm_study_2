import sys; sys.stdin=open('boj_14503_로봇청소기.txt')

'''
문제 & 출력 : 청소하는 영역의 개수
입력 : 세로 N, 가로 M / 좌표 r, c, 방향 d / 배열
풀이 : BFS, visit, 현재 방향을 기준으로 왼쪽 방향부터 탐색;
    
'''
# d = 0,1,2,3 >> 북,동,남,서
# if d = 0: 왼쪽은 서 남동 3 21 (d+3)%4  d += 1
# if d = 1: 왼쪽은 북 서남 0 32 #반대 (d+2)%4
# if d = 2: 왼쪽은 동 북서 1 03
# if d = 3: 왼쪽은 남 동북 2 10
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def BFS(sr,sc,ds):
    q = [(sr,sc)]
    visit = [[0]*M for _ in range(N)]
    visit[sr][sc] = 1
    d = ds
    while q:
        r, c = q.pop(0)
        #탐색
        f = 0
        for i in range(4):
            d = (d + 3) % 4
            nr, nc = r + dr[d], c + dc[d]

            if nr<0 or nr>=N or nc<0 or nc>=M: continue;
            if not arr[nr][nc] and not visit[nr][nc]:
                q.append((nr,nc))
                visit[nr][nc] = visit[r][c] + 1
                f = 1
                break

        if not f:
            d = (d + 2) % 4
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M and arr[nr][nc]:
                return visit
            q.append((nr,nc))

    return visit
N, M = map(int,input().split())
R, C, D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = BFS(R,C,D)
print(ans)
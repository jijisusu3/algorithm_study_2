import sys; sys.stdin=open('swea_벽돌깨기.txt')

def bomb(k, count, arr):
    global ans
    if k == N or count == 0:
        ans = min(ans, count)
        return

    else:
        for w in range(W):
            Q = []
            for h in range(H):
                if arr[h][w]:
                    pan = [a[:] for a in arr]
                    cnt = count - 1
                    # pan이 갱신되니까 cnt도 다른 변수에 넣어서 돌려줘야함.
                    Q = [(h,w,pan[h][w])]
                    pan[h][w] = 0
                    break
            if not Q: continue;

            # 블록 부수는 BFS
            while Q:
                r, c, v = Q.pop(0)
                for d in range(1, v):
                    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                        nr, nc = r + dr*d, c + dc*d
                        if 0<= nr < H and 0<= nc < W and pan[nr][nc]:
                            if pan[nr][nc] > 1:
                                Q.append((nr,nc,pan[nr][nc]))
                            pan[nr][nc] = 0
                            cnt -= 1


            # 중력작용.
            for x in range(W):
                idx = H - 1
                for y in range(H-1, -1, -1):
                    if pan[y][x]:
                        pan[idx][x], pan[y][x] = pan[y][x], pan[idx][x]
                        idx -= 1

            bomb(k+1, cnt, pan)

T = int(input())
for t in range(1,1+T):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    # 구슬을 떨어뜨려 순열필요하다.
    # 최소로 남아있는 값.
    count = 0
    for i in arr:
        for j in i:
            if j:
                count += 1
    ans = int(1e9) # 0xffffff
    bomb(0,count,arr)
    print(f'#{t}',ans)



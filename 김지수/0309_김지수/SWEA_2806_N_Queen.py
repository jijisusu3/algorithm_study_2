import sys
sys.setrecursionlimit(10000)


def bfs(row, col):
    if row == N:
        global cnt
        cnt += 1
    else:
        for i in range(N):
            if can_go[i] == 0 and i != col + 1 and i != col - 1:
                can_go[i] = 1
                bfs(row + 1, i)
                can_go[i] = 0


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    can_go = [0]*N
    cnt = 0
    bfs(0, 0)
    print(f'#{tc} {cnt}')




import sys; sys.stdin = open('123.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def oo(i):
    global rst




T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    high = []
    height = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height:
                height = arr[i][j]
                high = []
                high.append((i, j))
            elif arr[i][j] == height:
                high.append((i, j))

    rst = 0
    for i in high:
        oo(i)
    
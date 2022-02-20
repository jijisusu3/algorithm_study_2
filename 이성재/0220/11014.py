import sys; sys.stdin = open('11014.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    lt = lb = r = 0
    rt = rb = l = 0
    for i in range(N - 1):
        for j in range(N - 1):


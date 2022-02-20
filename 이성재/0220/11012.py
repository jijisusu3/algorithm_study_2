import sys; sys.stdin = open('11012.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_s = [list(map(int, input().split())) for _ in range(M)]


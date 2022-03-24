import sys; sys.stdin = open('2636.txt')

def cheeze(arr):
    if 1 not in arr:
        return
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


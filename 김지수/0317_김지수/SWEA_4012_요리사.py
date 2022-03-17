import sys
sys.stdin = open('4012.txt')


def subset(k):
    global result
    if k == N:
        if len(A) == len(B):
            print(A, B)
    else:
        A.append(k)
        subset(k + 1)
        A.pop()
        B.append(k)
        subset(k + 1)
        B.pop()


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    A, B = [], []
    result = 0
    subset(0)
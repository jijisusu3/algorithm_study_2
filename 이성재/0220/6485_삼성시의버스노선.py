import sys; sys.stdin = open('6485.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus = [0] * 5000
    for j in range(1, N + 1):
        A, B = map(int, input().split())
        for k in range(A - 1, B):
            bus[k] += 1
    P = int(input())
    result = [0] * P
    for j in range(P):
        C = int(input())
        result[j] = bus[C - 1]

    print('#{}'.format(tc), end=' ')
    print(*result)
        
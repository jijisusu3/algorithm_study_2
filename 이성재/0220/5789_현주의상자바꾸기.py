import sys; sys.stdin = open('5789.txt')

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())

    box = [0] * N
    for j in range(1, Q + 1):
        L, R = map(int, input().split())
        for k in range(L - 1, R):
            box[k] = j
    print('#{}'.format(tc), end=' ')
    print(*box)
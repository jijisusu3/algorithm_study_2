import sys; sys.stdin = open('1860.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    result = 'Possible'
    for i in range(N):
        cnt = (arr[i] // M) * K
        if cnt < i + 1:
            result = 'Impossible'
            break

    print('#{} {}'.format(tc, result))
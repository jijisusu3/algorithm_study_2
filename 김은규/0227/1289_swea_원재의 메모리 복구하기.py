import sys; sys.stdin = open('1289.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    memo = list(map(int, input()))
    N = len(memo)
    NUM = [0] * N

    cnt = 0
    for i in range(N):
        if NUM[i] == memo[i]:
            pass

        else:
            for j in range(i, N):
                NUM[j] = memo[i]
            cnt += 1

    print(f'#{tc} {cnt}')


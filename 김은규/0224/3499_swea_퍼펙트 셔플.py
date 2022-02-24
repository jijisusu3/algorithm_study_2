import sys; sys.stdin = open('3499.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = input().split()
    NN = N // 2

    if N % 2 == 0:
        a = lst[: NN]
        b = lst[NN : N]

    # N이 홀수일 경우 먼저 놓는 쪽에 더 많은 카드 분배
    else:
        a = lst[: NN+1]
        b = lst[NN+1 : N+1]


    result = []
    for i in range(N):
        if i % 2 == 0:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    print(f'#{tc}', end=' ')
    print(*result)

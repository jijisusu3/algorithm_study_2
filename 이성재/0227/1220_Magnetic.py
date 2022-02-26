import sys; sys.stdin = open('1220.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    num = 0
    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                for k in range(j + 1, N):
                    if arr[k][i] == 1:
                        break
                    elif arr[k][i] == 2:
                        num += 1
                        break

    print('#{} {}'.format(tc, num))
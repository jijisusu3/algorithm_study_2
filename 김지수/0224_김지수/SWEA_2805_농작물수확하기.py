import sys; sys.stdin = open('2805.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = sum(arr[N//2])
    cnt = 0
    mid_r = N//2
    x = 1
    y = 1
    while cnt < (N-1)/2:
        result += sum(arr[mid_r - x][y:N - y])
        result += sum(arr[mid_r + x][y:N - y])
        x += 1
        y += 1
        cnt += 1
    print(f'#{tc} {result}')
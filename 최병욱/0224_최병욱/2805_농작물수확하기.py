import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    total = 0
    for j in range(N):
        total += arr[N//2][j]
    for i in range(N//2):
        for k in range(N//2-i, N//2+i+1):
            total += arr[i][k]
            total += arr[N-1-i][k]
    print(f'#{test_case} {total}')

# 14 0 54 1 N//2 = 5//2 = 2
# 4 425 0 3 i = 1
#  02032 5
# 5 120 4 3 i = 3 = N - 1 - i = 5 - 1 - 1
# 52 2 12 1 i = 4 = N- 1 - i = 5 - 1- 0
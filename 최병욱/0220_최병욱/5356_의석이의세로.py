import sys
sys.stdin = open('5356.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    for j in range(max_len):
        for i in range(5):
            if len(arr[i]) <= j:
                continue
            else:
                print(arr[i][j], end = '')
    print()
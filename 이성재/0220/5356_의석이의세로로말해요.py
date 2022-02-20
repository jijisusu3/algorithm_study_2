import sys; sys.stdin = open('5356.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    max_len = 0
    for i in range(5):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])

    for i in range(5):
        while len(arr[i]) < max_len:
            arr[i].append('11')

    print('#{}'.format(tc), end=' ')
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] != '11':
                print(arr[j][i], end='')
    print()
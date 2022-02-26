import sys; sys.stdin = open('1289.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))

    if arr[0] == 1:
        cnt = 1
    else:
        cnt = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            cnt += 1


    print('#{} {}'.format(tc, cnt))
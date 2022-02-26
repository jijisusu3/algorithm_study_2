import sys; sys.stdin = open('1974.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    for i in range(9):
        if result == 0:
            break
        arr_a = []
        arr_b = []
        for j in range(9):
            if arr[i][j] in arr_a:
                result = 0
                break
            else:
                arr_a.append(arr[i][j])

            if arr[j][i] in arr_b:
                result = 0
                break
            else:
                arr_b.append(arr[j][i])

    for p in range(3):
        if result == 0:
            break
        for i in range(3):
            arr_c = []
            for j in range(3):
                for k in range(3):
                    if arr[j + 3 * p][k + 3 * i] in arr_c:
                        result = 0
                        break
                    else:
                        arr_c.append(arr[j + 3 * p][k + 3 * i])

    print('#{} {}'.format(tc, result))
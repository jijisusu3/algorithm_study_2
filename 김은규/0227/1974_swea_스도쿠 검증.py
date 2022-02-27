import sys; sys.stdin = open('1974.txt', 'r')

def sudoku(arr):
    for i in range(9):
        check = [0] * 10
        for j in range(9):
            if check[arr[i][j]] == 1:
                return 0

            else:
                check[arr[i][j]] = 1

    for i in range(9):
        check = [0] * 10
        for j in range(9):
            if check[arr[j][i]] == 1:
                return 0

            else:
                check[arr[j][i]] = 1

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = [0] * 10
            for a in range(3):
                for b in range(3):
                    if check[arr[i+a][j+b]] == 1:
                        return 0
                    else:
                        check[arr[i+a][j+b]] = 1

    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku(arr)
    print(f'#{tc} {result}')



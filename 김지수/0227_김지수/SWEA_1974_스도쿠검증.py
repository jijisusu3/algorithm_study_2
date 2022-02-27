import sys; sys.stdin = open('1974.txt')

TC = int(input())
for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    breaker = False
    for r in range(9): # 가로
        temp = []
        for c in range(9):
            if arr[r][c] in temp:
                breaker = True
                break
            else:
                temp.append(arr[r][c])

    if not breaker: # 세로
        for col in range(9):
            temp = []
            for row in range(9):
                if arr[row][col] in temp:
                    breaker = True
                    break
                else:
                    temp.append(arr[row][col])

    if not breaker:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                temp = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if arr[k][l] in temp:
                            breaker = True
                            break
                        else:
                            temp.append(arr[k][l])
    if breaker:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')

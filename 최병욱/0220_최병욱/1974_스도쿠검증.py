import sys
sys.stdin = open('1974.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    nums = list(range(1, 10))
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 행 우선순회
    flag = False
    for i in range(9):
        cnts = [0] * 10
        for j in range(9):
            cnts[arr[i][j]] += 1
        for k in range(1, 10):
            if cnts[k] != 1:
                print(0)
                flag = True
                break
        if flag:
            break
    if flag:
        continue
    for j in range(9):
        cnts = [0] * 10
        for i in range(9):
            cnts[arr[i][j]] += 1
        for k in range(1, 10):
            if cnts[k] != 1:
                print(0)
                flag = True
                break
        if flag:
            break
    if flag:
        continue
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            cnts = [0] * 10
            for k in range(3):
                for n in range(3):
                    cnts[arr[i+k][j+n]] += 1
            for m in range(1, 10):
                if cnts[m] != 1:
                    print(0)
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        continue
    print(1)

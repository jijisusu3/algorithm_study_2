# SWEA(10593)

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    max_num = 0
    row = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        add_row = sum(arr[r])
        for c in range(N):
            add_col = 0
            for i in range(N):
                add_col += arr[i][c]
            if add_row + add_col - arr[r][c] > max_num:
                max_num = add_row + add_col - arr[r][c]
    print(f'#{tc} {max_num}')


# 10989
TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    add = 0
    for _ in range(M):
        row, col, power = map(int, input().split())
        for i in range(row-power, row + power + 1): # y축 더하기
            if 0 <= i < N:
                add += arr[i][col]
                arr[i][col] = 0

        for j in range(col - power, col + power + 1): # x축 더하기
            if 0 <= j < N:
                add += arr[row][j]
                arr[row][j] = 0

    print(f'#{tc} {add}')


# 11010

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for r in range(N):
        for c in range(N):
            i1 = i2 = i3 = i4 = 1
            j1 = j2 = j3 = j4 = 1
            add = arr[r][c]
            while c - i1 >= 0 and r - j1 >= 0: # 1
                add += arr[r-j1][c-i1]
                i1 += 1
                j1 += 1
            while c - i2 >= 0 and r + j2 < N:
                add += arr[r + j2][c-i2]
                i2 += 1
                j2 += 1
            while c + i3 < N and r - j3 >= 0:
                add += arr[r-j3][c+i3]
                i3 += 1
                j3 += 1
            while c + i4 < N and r + j4 < N:
                add += arr[r+j4][c+i4]
                i4 += 1
                j4 += 1
            if add > max_num:
                max_num = add
    print(f'#{tc} {max_num}')


# 11012
TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    add = 0
    for _ in range(M):
        row, col, width = map(int, input().split())
        for i in range(width):
            for j in range(width):
                if row + i < N and col + j < N:
                    add += arr[row+i][col+j]
                    arr[row+i][col+j] = 0
    print(f'#{tc} {add}')

# 11013
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 21
    for i in range(N-2): # 첫번째 자르는 애 올 수 있는 정도
        temp1 = arr[:i+1]
        lst1 = sum(temp1)
        for j in range(i+1, N-1): # 두번째 자르는 애가 올 수 있는 정도
            temp2 = arr[i+1:j+1]
            lst2 = sum(temp2)
            temp3 = arr[j+1:]
            lst3 = sum(temp3)
            temp = [lst1, lst2, lst3]
            diff = abs(max(temp)-min(temp))
            if result > diff:
                result = diff
    print(f'#{tc} {result}')
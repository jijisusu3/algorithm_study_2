import sys; sys.stdin = open('2477.txt')

K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

area = 0
arr_num = [0] * 4
for i in range(6):
    if arr[i][0] == 1:
        arr_num[0] += 1
    elif arr[i][0] == 2:
        arr_num[1] += 1
    elif arr[i][0] == 3:
        arr_num[2] += 1
    else:
        arr_num[3] += 1

while arr_num[arr[0][0] - 1] != 1 or arr_num[arr[5][0] - 1] != 1:
    arr.append(arr.pop(0))

area = arr[0][1] * arr[5][1] - arr[2][1] * arr[3][1]

print(area * K)
# 1096_바둑판에 흰돌 놓기(코드업)

import sys; sys.stdin = open('1096.txt')

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

white = [[0] * 19 for _ in range(19)]
for i in range(T):
    a = arr[i][0]
    b = arr[i][1]
    white[a - 1][b - 1] = 1

for i in white:
    print(*i)


# 10816_숫자카드2(백준)

T = int(input())
arr_a = list(map(int, input().split()))
N = int(input())
arr_b = list(map(int, input().split()))

for i in range(len(arr_a)):
    for j in range(i + 1, len(arr_a)):
        if arr_a[i] > arr_a[j]:
            arr_a[i], arr_a[j] = arr_a[j], arr_a[i]

for i in arr_b:
    cnt = 0
    for j in range(len(arr_a)):
        if i == arr_a[j]:
            cnt += 1
            if i != arr_a[j]:
                break
    print(cnt, end=' ')


# 2805_나무자르기(백준)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_t = 0
for i in arr:
    if i > max_t:
        max_t = i

T = 0
a = max_t
while T <= a:
    mid = (T + a) // 2
    tree = 0
    for i in arr:
        if i >= mid:
            tree += i - mid
    if tree >= M:
        T = mid + 1
    else:
        a = mid - 1
print(a)
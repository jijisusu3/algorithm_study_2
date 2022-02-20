# 달팽이 again...

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
house = [[0]*m for _ in range(n)]
snail = n*m
r = 0
c = 0
d = 0

for snail in range(m*n, 0, -1):
    house[r][c] = snail
    r += dr[d]
    c += dc[d]
    if r >= n or c >= m or house[r][c] != 0:
        r -= dr[d]
        c -= dc[d]
        d = (d+1) % 4
        r += dr[d]
        c += dc[d]

for i in house:
    print(*i)


# code up (1515): 생명 게임 1

now_arr = [[0] * 27 for i in range(27)]
next_arr = [[0] * 27 for i in range(27)]

for i in range(1, 26):
    input_list = list(map(int, input().split()))
    for j in range(0, 25):
        now_arr[i][j + 1] = input_list[j]


def find(x, y):
    cnt = 0
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        if now_arr[x + dr[i]][y + dc[i]] == 1:
            cnt += 1
    return cnt


for r in range(1, 26):
    for c in range(1, 26):
        if now_arr[r][c] == 0 and find(r, c) == 3:
            next_arr[r][c] = 1
        if now_arr[r][c] == 1 and (find(r, c) >= 4 or find(r, c) <= 1):
            next_arr[r][c] = 0
        if now_arr[r][c] == 1 and (find(r, c) == 2 or find(r, c) == 3):
            next_arr[r][c] = 1

for i in range(1, 26):
    for j in range(1, 26):
        print(next_arr[i][j], end=' ')
    print()


# 블랙잭

# 시간초과
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

max_num = 0
for i in range(1 << N):
    temp_lst = []
    for j in range(N):
        if i & (1 << j):
            temp_lst.append(arr[j])
    if len(temp_lst) == 3:
        temp_add = sum(temp_lst)
        if max_num < temp_add <= M:
            max_num = temp_add
print(max_num)


# for문 이용
result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])
print(result)


# programmers : 정렬 : k번째 수

def select(lst, th):
    for i in range(0, th):
        x = i
        for j in range(i + 1, len(lst)):
            if lst[x] > lst[j]:
                x = j
        lst[i], lst[x] = lst[x], lst[i]
    return lst[th-1]


def solution(array, commands):
    answer = []
    arr = array
    for i, j, k in commands:
        new_arr = arr[i-1:j]
        th_num = select(new_arr, k)
        answer.append(th_num)
    return answer


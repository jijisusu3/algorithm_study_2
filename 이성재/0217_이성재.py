# 42748_K번째수

def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        arr = []
        for n in range(i - 1, j):
            arr.append(array[n])
        for n in range(len(arr)):
            for m in range(n + 1, len(arr)):
                if arr[n] > arr[m]:
                    arr[n], arr[m] = arr[m], arr[n]
        answer.append(arr[k-1])
    return answer


# 2798_블랙잭

import sys; sys.stdin = open('2798.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_num = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if max_num < arr[i] + arr[j] + arr[k] <= M:
                max_num = arr[i] + arr[j] + arr[k]

print(max_num)


# 1485_2차원 배열 달팽이 채우기

import sys; sys.stdin = open('1485.txt')

n, m = map(int, input().split())

snail = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, (m - 1)
k = 0

N = n * m
for i in range(N, N - m, -1):
    snail[0][N - i] = i

t = n - 1
p = m - 1
q = N - m

while p >= 0 and t >= 0:
    k += 1
    mode = k % 4
    if mode % 2 == 1:
        for i in range(t):
            x += dx[mode]
            y += dy[mode]
            snail[x][y] = q
            q -= 1
        t -= 1
    else:
        for j in range(p):
            x += dx[mode]
            y += dy[mode]
            snail[x][y] = q
            q -= 1
        p -= 1

for i in snail:
    print(*i)


# 1515_생명게임1 - 아직..

import sys; sys.stdin = open('1515.txt')

arr = [[0] * 27] + [[0] + list(map(int, input().split() + [0])) for _ in range(25)] + [[0] * 27]

def arr_num(a, b):
    cnt = 0
    1 <= a <= 25
    1 <= b <= 25
    for i in range(-1, 2):
        for j in range(-1, 2):    
            if arr[a + i][b + j] == 1:
                cnt += 1
    return cnt

for x in range(1, 26):
    for y in range(1, 26):
        if arr_num(x, y) == 3 and arr[x][y] == 0:
            arr[x][y] = 1
        elif arr[x][y] == 1 and arr_num(x, y) <= 2 >= 5:
            arr[x][y] = 0
        elif arr[x][y] == 1 and arr_num(x, y) >= 5:
            arr[x][y] = 0
        elif arr[x][y] == 1 and arr_num(x, y) == 4:
            arr[x][y] = 1
        elif arr[x][y] == 1 and arr_num(x, y) == 3 == 4:
            arr[x][y] = 1
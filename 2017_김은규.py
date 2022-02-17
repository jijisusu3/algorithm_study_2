# K번째 수

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = array[i-1: j]
        for a in range(len(arr)-1, -1, -1):
            for b in range(0, a):
                if arr[b] > arr[b+1]:
                    arr[b], arr[b+1] = arr[b+1], arr[b]
        answer.append(arr[k - 1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

# =========================================================

# 블랙잭

import sys; sys.stdin = open('2798.txt', 'r')

n, m = map(int, input().split())
num = list(map(int, input().split()))
len_n = len(num)
lst = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] <= m:
                lst.append(num[i] + num[j] + num[k])

max_v = 0
for i in lst:
    if i >= max_v:
        max_v = i

print(max_v)

# =============================================================

# 2차원 배열 달팽이 채우기

import sys; sys.stdin = open('2798.txt', 'r')

n, m = map(int, input().split())
num = list(map(int, input().split()))
len_n = len(num)
lst = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] <= m:
                lst.append(num[i] + num[j] + num[k])

max_v = 0
for i in lst:
    if i >= max_v:
        max_v = i

print(max_v)

# ===============================================================


import sys

T = int(input())
lst = list(map(int, sys.stdin.readline().split('/n')))
max_v = 0
for i in lst:
    if i > max_v:
        max_v = i
B = [0] * (max_v+1)
C = [0] * (len(lst))

for val in lst: # 카운팅
    B[val] += 1

for i in range(1, max_v+1): # 누적
    B[i] = B[i-1] + B[i]

for i in range(len(lst)-1, -1, -1):
    B[lst[i]] -= 1
    C[B[lst[i]]] = lst[i]

for i in C:
    print(i)
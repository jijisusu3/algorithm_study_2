import sys
N = int(sys.stdin.readline()) # N = 10
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))  # lst = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]
max_v = 0
for i in lst:
    if i > max_v:
        max_v = i
B = [0] * (max_v+1)
C = [0] * (len(lst))

for val in lst: # 카운팅 B : [0, 2, 2, 2, 1, 2, 0, 1]
    B[val] += 1

for i in range(1, max_v+1): # 누적 B : [0, 2, 4, 6, 7, 9, 9, 10]
    B[i] = B[i-1] + B[i]

for i in range(len(lst)-1, -1, -1): # C : [1, 1, 2, 2, 3, 3, 4, 5, 5, 7]
    B[lst[i]] -= 1
    C[B[lst[i]]] = lst[i]

for i in C:
    print(i)

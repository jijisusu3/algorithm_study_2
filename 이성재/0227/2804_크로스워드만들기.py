import sys; sys.stdin = open('2804.txt')

A, B = map(str, input().split())

a = 0
b = 0
flag = False
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            a, b = i, j
            flag = True
            break
    if flag == True:
        break

arr = [list('.' * (len(A))) for _ in range(len(B))]

for i in range(len(A)):
    arr[b][i] = A[i]

for i in range(len(B)):
    arr[i][a] = B[i]

for i in range(len(B)):
    for j in range(len(A)):
        print(arr[i][j], end='')
    print()
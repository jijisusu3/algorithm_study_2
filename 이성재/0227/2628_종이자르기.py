import sys; sys.stdin = open('2628.txt')

A, B = map(int, input().split())
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

for i in range(T - 1):
    for j in range(i, T):
        if arr[i][1] > arr[j][1]:
            arr[i], arr[j] = arr[j], arr[i]

a = 0
b = A
list_a = []
c = 0
d = B
list_b = []
for i in range(T):
    if arr[i][0] == 1:
        list_a.append(arr[i][1] - a)
        a = arr[i][1]
    elif arr[i][0] == 0:
        list_b.append(arr[i][1] - c)
        c = arr[i][1]
for i in list_a:
    b -= i
list_a.append(b)
for i in list_b:
    d -= i
list_b.append(d)

list_a.sort()
list_b.sort()

print(list_a[-1] * list_b[-1])

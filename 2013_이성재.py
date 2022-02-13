# 2039 일곱 난쟁이

arr = []
for tc in range(1, 10):
    arr.append(int(input()))

for i in range(9):
    for j in range(i, 9):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

sum_arr = 0
for i in arr:
    sum_arr += i

for i in range(8):
    for j in range(i + 1, 9):
        if len(arr) < 9:
            break
        if sum_arr - arr[i] - arr[j] == 100:
            arr.pop(i)
            arr.pop(j - 1)            
            for k in arr:
                print(k)


# 10972 다음순열

T = int(input())
arr = list(map(int, input().split()))
n = 0
for i in range(T - 1, 0, -1):
    if arr[i - 1] < arr[i]:
        for j in range(T - 1, 0, -1):
            if arr[i - 1] < arr[j]:
                arr[i - 1], arr[j] = arr[j], arr[i - 1]
                for k in range(i, T - 1):    # sorted..
                    for t in range(i + 1, T):
                        if arr[k] > arr[t]:
                            arr[k], arr[t] = arr[t], arr[k]
                n = 1
                break
    if n == 1:
        print(*arr)  #....
        break
else:
    print(-1)


# 9095 1,2,3더하기

T = int(input())
arr = []
for tc in range(1, T + 1):
    arr.append(int(input()))

def sum_a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sum_a(n - 1) + sum_a(n - 2) + sum_a(n - 3)

for i in arr:
    print(sum_a(i))
import sys; sys.stdin = open('1208.txt')


for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    while cnt < T:
        num = 0
        for i in range(100):
            for j in range(i + 1, 100):
                if arr[i] > arr[j]:
                    num = arr[i]
                    arr[i] = arr[j]
                    arr[j] = num
        
        arr[99] = arr[99] - 1
        arr[0] = arr[0] + 1
        cnt += 1
    for i in range(100):
        for j in range(i + 1, 100):
            if arr[i] > arr[j]:
                num = arr[i]
                arr[i] = arr[j]
                arr[j] = num
    
    a = arr[99] - arr[0]

    print('#{} {}'.format(tc, a))
for num in range(1,11):
    dumps = int(input())
    arr = list(map(int,input().split()))
    # 일단 비효율적인거 알겠고...
    #정렬하고
    # dumps 반복하여
    #맨 뒤 -1 맨 앞 +1
    #다시 정렬
    for j in range(len(arr), 0, -1):
        for i in range(1, j):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
 
    for i in range(dumps):
        arr[-1]-=1
        arr[0]+=1
        for j in range(len(arr), 0, -1):
            for i in range(1, j):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
    print(f'#{num} {arr[-1] - arr[0]}')
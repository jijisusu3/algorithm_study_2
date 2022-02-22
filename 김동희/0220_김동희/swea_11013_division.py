import sys; sys.stdin = open('swea_11013_division.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    diff_lst = []

    for i in range(N-2):
        sec1 = sum(arr[:i+1])

        for j in range(i+1, N-1):
            sec2 = sum(arr[i+1:j+1])
            sec3 = sum(arr[j+1:])

            sector = [sec1, sec2, sec3]
            diff = max(sector)-min(sector)
            diff_lst.append(diff)

    result = min(diff_lst)
    print(f'#{tc} {result}')
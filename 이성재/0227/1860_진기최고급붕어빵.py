import sys; sys.stdin = open('1860.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    a = 'Possible'  # 아래에서 'Impossible'만 찾기 위해서
    cnt = 0   # 빵 개수
    for i in range(arr[-1] + 1):
        while i > arr[0] or arr == []:
            cnt -= 1
            arr.pop(0)

        if i % M == 0 and i != 0:
            cnt += K

        if i == arr[0]:
            if cnt <= 0:
                a = 'Impossible'
                break
            else:
                cnt -= 1
                arr.pop(0)

    print('#{} {}'.format(tc, a))


# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     arr.sort()
#
#     result = 'Possible'
#     for i in range(N):
#         cnt = (arr[i] // M) * K
#         if cnt < i + 1:
#             result = 'Impossible'
#             break
#
#     print('#{} {}'.format(tc, result))
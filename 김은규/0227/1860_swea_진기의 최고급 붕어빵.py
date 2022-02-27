import sys; sys.stdin = open('1860.txt', 'r')

def solve(arr):
    # 특정시간에 몇개의 붕어빵이 팔렸는지 알 수 있도록 정렬
    arr.sort()
    # 붕어 빵을 살 수 있다 -> (현재시간에 만들 수 있는 개수 - 이전 손님 수) > 1
    for i in range(N):
        # 붕어빵을 만들수 있는 개수 = arr[i]//M(붕어빵을 만들수 있는 횟수) * K
        if (arr[i]//M)*K - i < 1:   # i 이전 손님 수
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 손님 N명, K개의 붕어빵을 만드는데 걸리는 시간 M,
    arr = list(map(int, input().split()))
    print(f'#{tc} {solve(arr)}')
import sys; sys.stdin = open('1220.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 교착상태 개수를 세기 위한 변수
    check = [0] * N  # 위에거 저장 배열
    for i in range(N):
        for j in range(N):
            # 두 가지 경우
            if arr[i][j] == 1:  # N극
                check[j] = 1
            elif arr[i][j] == 2:  # s극
                if check[j] == 1:
                    result += 1
                check[j] = 2

    print(f'#{tc} {result}')
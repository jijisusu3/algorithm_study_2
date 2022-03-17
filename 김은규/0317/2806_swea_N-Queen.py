import sys; sys.stdin = open('2806.txt', 'r')

# 1차원 배열 생성 후 col[i]의 값이 j 라고 한다면 i행의 j열에 퀸이 있다는 의미.
# 기본 : 같은 행에 퀸을 놓지 않는다.
# 추가 : 같은 열 col[i] == col[k], 같은 대각선 col[i] - col[k] == i - k 에 놓이는지 확인
# 결구 못풀고 다른사람 풀이 참고...

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    row = [0] * n

    def is_promising(x):
        for i in range(x):
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
                return False
        return True


    def n_queens(x):
        global cnt
        if x == n:
            cnt += 1

        else:
            for i in range(n):
                row[x] = i  # 인덱스 x가 퀸의 행 위치, i가 열 위치
                if is_promising(x):  # true 일 경우 백트래킹 하지 않고, 계속 진행
                    n_queens(x + 1)

    n_queens(0)
    print(f'#{tc} {cnt}')
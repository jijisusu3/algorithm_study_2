import sys
sys.stdin = open('4012.txt')


def subset(k):
    global result
    if k == N:
        if len(A) == len(B):
            total_A = 0
            total_B = 0
            for i in range(N // 2 - 1):
                for j in range(i + 1, N // 2):
                    # A
                    total_A += foods[A[i]][A[j]]
                    total_A += foods[A[j]][A[i]]
                    # B
                    total_B += foods[B[i]][B[j]]
                    total_B += foods[B[j]][B[i]]
            temp = abs(total_A - total_B)
            if temp < result:
                result = temp

    else:
        A.append(k)
        subset(k + 1)
        A.pop()
        B.append(k)
        subset(k + 1)
        B.pop()


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    A, B = [], []
    result = 20000
    subset(0)
    print(f'#{tc} {result}')
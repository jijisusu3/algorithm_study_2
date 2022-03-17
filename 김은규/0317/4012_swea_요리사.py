import sys ; sys.stdin = open('4012.txt', 'r')

ANS =[]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    for subset in range(1 << (N -1)):
        cnt = 0
        A, B = [], []
        for i in range(N):
            if subset & (1 << i):
                A.append(i)
            else:
                B.append(i)

        if len(A) == len(B):

            sum_A = 0
            for i in range(len(A)):
                for j in range(i + 1, len(A)):
                    sum_A += arr[A[i]][A[j]] + arr[A[j]][A[i]]
            sum_B = 0
            for i in range(len(B)):
                for j in range(i + 1, len(B)):
                    sum_B += arr[B[i]][B[j]] + arr[B[j]][B[i]]

            if ans == -1:
                ans = abs(sum_A - sum_B)
            else:
                ans = min(ans, abs(sum_A - sum_B))
    ANS.append(ans)

for i in range(T):
    print(f'#{i + 1} {ANS[i]}')
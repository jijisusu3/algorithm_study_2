import sys; sys.stdin = open('2804.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = map(list, input().split())
    N = len(A)
    M = len(B)
    arr = [['.']*N for _ in range(M)]

    for i in range(N):
        if A[i] in B:
            idx_A = i  # 1
            word = A[i]  # A
            break

    for i in range(M):
        if B[i] in A:
            idx_B = i  # B
            break

    for i in range(M):
        for j in range(N):
            arr[idx_B][idx_A] = word

    for i in range(M):
        if arr[i][idx_A] == '.':
            arr[i][idx_A] = B.pop(0)

        else:
            B.pop(0)

    for i in range(N):
        if arr[idx_B][i] == '.':
            arr[idx_B][i] = A.pop(0)

        else:
            A.pop(0)


    for i in range(M):
        for j in range(N):
            print(arr[i][j], end='')
        print()

    '''for lst in arr:
        print(*lst)
    print()'''
import sys; sys.stdin = open('1289.txt')

TC = int(input())
for tc in range(1, TC+1):
    cnt = 0
    lst = list(map(int, input()))
    N = len(lst)
    new = [0]*N
    for i in range(N-1):
        if new[i] != lst[i]:
            new[i] = lst[i]
            cnt += 1
            if lst[i] == 0:
                for x in range(i+1, N):
                    new[x] = lst[i]
            else:
                for y in range(i+1, N):
                    new[y] = lst[i]
    if new[-1] != lst[-1]:
        cnt += 1

    print(f'#{tc} {cnt}')



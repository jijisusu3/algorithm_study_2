import sys;

sys.stdin = open('1860.txt')


TC = int(input())
for tc in range(1, TC + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(len(lst)-1, -1, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    last = lst[-1]
    bread = 0
    timer = 0
    if lst[0] < M:
        print(f'#{tc} Impossible')
    else:
        breaker = False
        for i in range(last):
            timer += 1
            if timer % M == 0:
                bread += K
            if lst[0] == timer:
                while lst and timer == lst[0]:
                    bread -= 1
                    lst.pop(0)
                    if bread < 0:
                        print(f'#{tc} Impossible')
                        breaker = True
                        break
            if breaker:
                break
        else:
            print(f'#{tc} Possible')








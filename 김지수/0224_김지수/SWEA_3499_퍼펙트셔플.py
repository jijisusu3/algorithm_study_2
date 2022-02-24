import sys; sys.stdin = open('3499.txt')

TC = int(input())
for tc in range(1, TC+1):
    print(f'#{tc} ', end='')
    N = int(input())
    lst = list(map(str, input().split()))
    middle = (N + 1)//2
    top = lst[:middle]
    bottom = lst[middle:]
    result = []
    for i in range(N//2):
        result.append(top.pop(0))
        result.append(bottom.pop(0))
    if top:
        result.append(top.pop(0))
    print(*result)

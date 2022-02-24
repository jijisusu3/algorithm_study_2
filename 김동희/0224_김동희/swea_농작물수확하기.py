import sys; sys.stdin=open('swea_농작물수확하기.txt')

TC = int(input())

for tc in range(1,1+TC):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    result = 0
    idx = N//2
    for r in range(idx+1): # 0 1 2
        for c in range(idx-r,idx+1+r): # 2 /  1,2,3 / 0,1,2,3,4 /
            result += arr[r][c]

    for r in range(N-1,idx,-1): # 4, 3
        for c in range(idx-N+r+1,idx+N-r): #  2 / 1 2 3
            result += arr[r][c]

    print(f'#{tc} {result}')





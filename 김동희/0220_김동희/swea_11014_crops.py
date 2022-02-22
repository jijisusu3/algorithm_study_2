import sys; sys.stdin = open('swea_11014_crops.txt')

TC = int(input())
for tc in range(1,1+TC):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    diff = []

    for r in range(N):
        for c in range(N):
            total += arr[r][c]

    for i in range(1,N):
        for j in range(1,N):

            part1 = 0

            for r in range(i):
                for c1 in range(j):
                    part1 += arr[r][c1]
                    part2 = 0
                    for r2 in range(j):
                        for c2 in range(N-1,i-1,-1):
                            part2 += arr[c2][r2]

            part3 = total-part1-part2
            diff.append((max(part1,part2,part3) - min(part1,part2,part3)))

    result = min(diff)
    print(f'#{tc} {result}')


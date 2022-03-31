import sys
sys.stdin = open('2115.txt')


def second(row):
    for x in range(N):
        for y in range(N - M + 1):
            tmp = []
            for z in range(y, y + M):
                if visited[x][z] == 1:
                    break
                else:
                    tmp.append(arr[x][z])
            else:
                a = temp_sum + tmp
                lst.append(a)


TC = int(input())
for tc in range(1, TC + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    lst = []
    result = 1000000000
    A = []
    B = []
    X = []
    for r in range(N):
        for c in range(N - M + 1):
            temp_sum = []
            for i in range(c, c + M):
                visited[r][i] = 1
                temp_sum.append(arr[r][i])
            second(r)
            visited = [[0]*N for _ in range(N)]
    print(lst)
    print()
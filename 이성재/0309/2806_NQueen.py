import sys; sys.stdin = open('2806.txt')

def dfs(idx, row):
    global N, cnt
    if row == N:
        cnt += 1
        return
    arr = [0] * N
    for i in range(len(idx)):
        arr[idx[i]] = 1
        if idx[i] - (row - i) >= 0:
            arr[idx[i] - (row - i)] = 1
        if idx[i] + (row - i) < N:
            arr[idx[i] + (row - i)] = 1
    for i in range(N):
        if arr[i] == 0:
            dfs(idx + [i], row + 1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    cnt = 0
    dfs([],0)
    print("#{} {}".format(tc, cnt))
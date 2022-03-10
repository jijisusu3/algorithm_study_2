import sys; sys.stdin = open('1012.txt', 'r')

# 아이디어
# 0으로 이루어진 2차원 배열 만든 후, 좌표값을 받아서 해당 좌표영역을 1로 바꿔준다.
# 2차원 배열에서 1을 찾은 후, bfs를 활용하여 해당 1이 위치한 구역의 개수를 센다(찾은 0은 1으로 변경)
# result에 값들을 저장하고 result의 개수를 출력한다

def BFS(i, j, arr):
    cnt = 1
    q = []
    q.append([i, j])
    arr[i][j] = 0

    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    cnt += 1
                    q.append([ni, nj])

    return cnt


T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    result = []
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                result.append(BFS(i, j, arr))

    print(len(result))
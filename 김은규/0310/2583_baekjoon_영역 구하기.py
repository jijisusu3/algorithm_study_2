import sys; sys.stdin = open('2583.txt', 'r')
# from collections import deque
# TypeError: descriptor 'append' for 'collections.deque' objects doesn't apply to a 'list' object

# 아이디어
# 0으로 이루어진 2차원 배열 만든 후, 좌표값을 받아서 해당 좌표영역을 1로 바꿔준다.
# 2차원 배열에서 0을 찾은 후, bfs를 활용하여 해당 0이 위치한 구역의 개수를 센다(찾은 0은 1으로 변경)
# 해당 값들을 리스트에 저장 후 오름차순으로 정렬 후 출력
def BFS(i, j, arr):
    cnt = 1
    q = []
    q.append([i, j])
    arr[i][j] = 1

    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    cnt += 1
                    q.append([ni, nj])
    return cnt

M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] = 1

result = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            result.append(BFS(i, j, arr))

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')



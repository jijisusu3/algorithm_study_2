import sys; sys.stdin = open('2667.txt', 'r')

# 아이디어
# 2차원 배열에서 1을 찾은 후, bfs를 활용하여 해당 1이 위치한 구역의 1의 개수를 센다(찾은 1은 0으로 변경)
# 해당 값들을 리스트에 저장 후 오름차순으로 정렬 후 출력

def bfs(i, j, arr):
    cnt = 1  # 처음 1로 시작
    queue = []
    queue.append([i, j])
    arr[i][j] = 0  # 1인 값을 0으로 변경


    while queue:
        i, j = queue.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    cnt += 1
                    queue.append([ni, nj])
    return cnt



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

result = []  # 7, 8, 9
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result.append(bfs(i, j, arr))

result.sort()

print(len(result))
for i in result:
    print(i)




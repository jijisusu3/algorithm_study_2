# 프로그래머스 K번째 수

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        array_cut = sorted(array[i-1 : j])
        answer.append(array_cut[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

# 백준 2798 블랙잭
import sys

# n, M = map(int, sys.stdin.readline().split())
# cards = list(map(int, sys.stdin.readline().split()))
# close = 0
# for i in range(1 << n):
#     cnt = 0
#     idx_lst = []
#     for j in range(n):
#         if i & 1 << j:
#             cnt += 1
#             idx_lst.append(j)
#     if cnt == 3:
#         total = 0
#         for idx in idx_lst:
#             total += cards[idx]
#         if total <= M:
#             if M - total < M - close:
#                 close = total
# print(close)
# 시간초과 -> 모든 경우의 수를 돌아서 그런가?


N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
close = 0
total = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:
                if M - total < M - close:
                    close = total
print(close)

# CodeUp 생명게임
arr = [list(map(int, input().split())) for _ in range(25)]
new_arr = [[0]*25 for _ in range(25)]
# 좌 우 상 하 대각 1, 2, 3, 4
di = [0, 0, -1, 1, -1, -1, 1, 1]
dj = [-1, 1, 0, 0, -1, 1, -1, 1]
N = 25
for i in range(N):
    for j in range(N):
        total = 0
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj <N:
                total += arr[ni][nj]
        if total == 3:
            new_arr[i][j] = 1
        elif total >= 4 or total <= 1:
            new_arr[i][j] = 0
        elif total == 2 or total == 3:
            if arr[i][j] == 1:
                new_arr[i][j] = 1

for i in range(25):
    for j in range(25):
        print(new_arr[i][j], end= ' ')
    print()


# CodeUp 달팽이
N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
r, c, n = 0, -1, N*M + 1
rs, cs = N, M
direction = 1
while rs > 0 and cs > 0:
    for _ in range(cs):
        n -= 1
        c += direction
        arr[r][c] = n
    rs -= 1
    for _ in range(rs):
        n -= 1
        r += direction
        arr[r][c] = n
    cs -= 1
    direction = -direction
for num in arr:
    for n in num:
        print(n, end = ' ')
    print()
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

# 회문1
T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    breaker = False
    for l in range(N):
        # 행 우선 순회
        for i in range(N-M+1):
            # abcdbca M = 7
            for j in range(M//2):
                if words[l][i + j] != words[l][i + M-j-1]:
                    break
            else: # 회문을 찾았을 때
                result = ''
                for k in range(i, i + M):
                    result += words[l][k]
                breaker = True
                break
        if breaker:
            print(result)
            break

        # 열 우선 순회
        for i in range(N-M + 1):
            for j in range(M//2):
                if words[i + j][l] != words[i + M-j-1][l]:
                    break
            else:
                result = ''
                for k in range(i, i + M):
                    result += words[k][l]
                breaker = True
                break
        if breaker:
            print(result)
            break

# a = 'bbab' # word -> b -> b -> a -> b
# for word in a:
#     if word == 'a':
#         print('a')
#         break
# else:
#     print('a가 없음')

# 회문2
T = 10
for test_case in range(1, T+1):
    tc = int(input())
    print(f'#{test_case}', end = ' ')
    words = [list(input()) for _ in  range(100)]
    max_len = 0
    for i in range(100):
        # 행 우선 순회
        # ABCCBAANDB i = 0 j = 0 ... 100
        for j in range(100):
            for M in range(100 - j + 1):
                for k in range(M//2):
                    if words[i][j + k] != words[i][j + M-k-1]:
                        break
                else: # 회문을 찾았을 때
                    if max_len < M:
                        max_len = M
        # 열 우선 순회
        for j in range(100):
            for M in range(1, 100 - j + 1):
                for k in range(M//2):
                    if words[j + k][i] != words[j + M-k-1][i]:
                        break
                else:
                    if max_len < M:
                        max_len = M
    print(max_len)


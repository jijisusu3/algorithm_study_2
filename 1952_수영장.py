import sys
sys.stdin = open('1952.txt', 'r')

# def DFS(n, ssum):
#     global ans
#     if n > 12:
#         if ans > ssum:
#             ans = ssum
#         return
#     DFS(n + 1, ssum + lst[n]*day)
#     DFS(n + 1, ssum + mon)
#     DFS(n + 3, ssum + mon3)
#     DFS(n + 12, ssum + year)
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     day, mon, mon3, year = map(int, input().split())
#     lst = [0] + list(map(int, input().split()))
#     # ans = 12345678
#     # DFS(1, 0)
#     # print(f'#{test_case} {ans}')
#     D = [0]*13
#     for i in range(1, 13):
#         mmin = D[i - 1] + lst[i]*day
#         mmin = min(mmin, D[i - 1] + mon)
#         if i >= 3:
#             mmin = min(mmin, D[i - 3] + mon3)
#         if i >= 12:
#             mmin = min(mmin, D[i - 12] + year)
#         D[i] = mmin
#     print(f'#{test_case} {D[12]}')


# # 교수님 풀이
# for tc in range(1, int(input()) + 1):
#     day, month, quarter, year = map(int, input().split())
#     arr = [0] + list(map(int, input().split()))
#     ans = year
#     def dfs(n, cost):
#         global ans
#
#         if n >= 13:
#             if ans > cost:
#                 ans = cost
#         else:
#             # n월에 요금을 지불
#             if arr[n] == 0:
#                 dfs(n + 1, cost)
#             else:
#                 dfs(n + 1, cost + arr[n] * day) # 일요금
#                 dfs(n + 1, cost + month) # 월요금
#                 dfs(n + 3, cost + quarter) # 분기요금
#     dfs(1, 0)
#     print(f'#{tc} {ans}')



# for tc in range(1, int(input()) + 1):
#     day, month, quarter, year = map(int, input().split())
#     arr = [0] + list(map(int, input().split()))
#     memo = [-1] * 13
#     def dfs(n):
#         global ans
#
#         if n == 0:
#             return 0
#
#         if memo[n] != -1:
#             return memo[n]
#
#         else:
#             a = b = c = year
#             if n >= 1:
#                 a = dfs(n - 1) + arr[n] * day # 일요금
#                 b = dfs(n - 1) + month # 월요금
#             if n >= 3:
#                 c = dfs(n - 3) + quarter # 분기요금
#             memo[n] = min(a, b, c)
#             return memo[n]
#
#     ans = dfs(12)
#     print(f'#{tc} {min(year, ans)}')


# for tc in range(1, int(input()) + 1):
#     day, month, quarter, year = map(int, input().split())
#     arr = [0] + list(map(int, input().split()))
#     memo = [year] * 13
#
#     memo[0] = 0
#     for n in range(1, 13):
#         a = b = c = year
#         if n >= 1:
#             a = memo[n - 1] + arr[n] * day # 일요금
#             b = memo[n - 1] + month # 월요금
#         if n >= 3:
#             c = memo[n - 3] + quarter # 분기요금
#         memo[n] = min(memo[n], a, b, c)
#
#     print(f'#{tc} {memo[12]}')
#
#
# for tc in range(1, int(input()) + 1):
#     day, month, quarter, year = map(int, input().split())
#     arr = [0] + list(map(int, input().split()))
#     memo = [year] * 13
#
#     memo[0] = 0
#     for n in range(1, 13):
#         a = b = c = year
#         if n >= 1:
#             a = memo[n - 1] + arr[n] * day # 일요금
#             b = memo[n - 1] + month # 월요금
#         if n >= 3:
#             c = memo[n - 3] + quarter # 분기요금
#         memo[n] = min(memo[n], a, b, c)
#
#     print(f'#{tc} {memo[12]}')

for tc in range(1, int(input()) + 1):
    day, month, quarter, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    memo = [year] * 13

    memo[0] = 0
    for n in range(1, 13):
        if arr[n]:
            a = b = c = year
            if n >= 1:
                a = memo[n - 1] + arr[n] * day # 일요금
                b = memo[n - 1] + month # 월요금
            if n >= 3:
                c = memo[n - 3] + quarter # 분기요금
            memo[n] = min(memo[n], a, b, c)
        else:
            memo[n] = memo[n - 1]

    print(f'#{tc} {memo[12]}')


for tc in range(1, int(input()) + 1):
    day, month, quarter, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    memo = [year] * 13

    memo[0] = 0
    for n in range(1, 13):
        if arr[n]:
            a = b = c = year
            if n >= 1:
                a = memo[n - 1] + arr[n] * day # 일요금
                b = memo[n - 1] + month # 월요금
            if n >= 3:
                c = memo[n - 3] + quarter # 분기요금
            memo[n] = min(memo[n], a, b, c)
        else:
            memo[n] = memo[n - 1]

    print(f'#{tc} {memo[12]}')

for tc in range(1, int(input()) + 1):
    day, month, quarter, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    memo = [year] * 13

    memo[0] = 0
    for n in range(1, 13):
        memo[n] = min(memo[n], memo[n - 1] + arr[n] * day)
        memo[n] = min(memo[n], memo[n - 1] + month)
        if n > 3 :
            memo[n] = min(memo[n], memo[n - 3] + quarter)

    print(f'#{tc} {memo[12]}')

import sys
N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
# print(N,M, arr)
result = 0
for i in range(1<<N):
    cnt = 0
    total = 0
    for j in range(N):
        if i & (1<<j):
            cnt += 1
            total += arr[j]
    if cnt == 3 and total <= M and total > result:
        result = total
print(result)


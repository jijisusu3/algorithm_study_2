import sys; sys.stdin = open('17298.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))
result = []

if max(lst) == lst[0]:  # lst 첫번째 값이 가장 크면 항상 -1
    result.append(-1)

for i in range(N):
    if i == N - 1:  # lst 끝 값은 항상 -1
        result.append(-1)

    else:
        for j in range(i+1, N):
            if lst[i] < lst[j]:
                result.append(lst[j])
                break

print(*result)

# 틀림... 반례가 있나?
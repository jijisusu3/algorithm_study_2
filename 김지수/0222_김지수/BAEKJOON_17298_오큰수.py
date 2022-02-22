# 이건 시간초과됨

import sys
N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
stack = []
for i in range(N-1): # 마지막일 때는 항상 -1이니까 빼고 계산
    max_num = lst[i]
    for j in range(i+1, N):
        if lst[j] > max_num:
            stack.append(lst[j])
            break
    else:
        stack.append(-1)
stack.append(-1)
print(*stack)


# 재시도
# import sys
# N = int(input())
# lst = list(map(int, sys.stdin.readline().split()))
# stack = []
# for i in range(N-1, -1, -1):
#     x = lst[i]
#     if

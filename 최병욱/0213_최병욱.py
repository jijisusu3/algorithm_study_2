# 백준(2309)
from random import randint

# 완전 탐색으로 안풀면 안되는건가?
N = 9
heights = []
for _ in range(N):
    heights.append(int(input()))

total = 0
for height in heights:
    total += height

for i in range(N-1):
    for j in range(0, N-i-1):
        if heights[j] > heights[j+1]:
            heights[j], heights[j+1] = heights[j+1], heights[j]

i = 0
ans = []
while i < N:
    k = 1
    while i + k < N:
        num = 0
        num += heights[i]
        num += heights[i+k]
        if total - num == 100:
            ans_lst = []
            heights[i] = heights[i+k] = 0
            for height in heights:
                if height != 0:
                    ans_lst.append(height)
            ans.append(ans_lst)
        k += 1
    i += 1
lst = ans[randint(0, len(ans)-1)]
for val in lst:
    print(val)

# 백준 10972
# N = int(input())
# nums = list(map(int, input().split()))
# N_lst = list(range(1, N+1))
# ans = [N_lst[:]]
#
# for i in range(N):
#     for j in range(N-1, i, -1):
#         if N_lst[j] > N_lst[j-1]:
#             N_lst[j], N_lst[j-1] = N_lst[j-1], N_lst[j]
#             copy_N_lst = N_lst[:] # deepcopy, shallow copy 주의
#             ans.append(copy_N_lst)
#
# for i in range(len(ans)-1):
#     if ans[i] == nums:
#         print(*ans[i+1])
#         break
# else:
#     print(-1)
# 메모리 초과

# N = int(input())
# nums = list(map(int, input().split()))
# for i in range(N):
#     if nums[i] != N-i:
#         for j in range(1, N-i):
#             if nums[i+j-1] != j:
#                 nums[i+j-1], nums[i+j-2] = nums[i+j-2], nums[i+j-1]
#                 print(*nums)
#                 quit()
#         else:
#             nums[N-1], nums[N-2] = nums[N-2], nums[N-1]
#             print(*nums)
#             quit()
# else:
#     print(-1)

# 백준 9095
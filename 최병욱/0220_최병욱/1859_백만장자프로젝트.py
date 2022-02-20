import sys
sys.stdin = open('1859.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    i = total = 0
    while len(nums) >= 1:
        max_num = max_idx = 0
        for idx, num in enumerate(nums):
            if max_num < num:
                max_num = num
                max_idx = idx
        for j in range(i, max_idx+1):
            total += max_num - nums[j]
        nums = nums[max_idx+1:]
    print(f'#{test_case} {total}')
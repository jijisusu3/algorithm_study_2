import sys
sys.stdin = open('11013.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    N = int(input())
    nums = list(map(int, input().split()))
    ans = []
    for i in range(1, N):
        for j in range(i+1, N):
            copy_num = nums[:]
            num = []
            split_num = []
            copy_num.insert(i, -11)
            copy_num.insert(j+1, -11)
            copy_num += [-11]
            k = 0
            while k < N + 3:
                if copy_num[k] != -11:
                    num.append(copy_num[k])
                else: # -11 벽을 만났을때
                    split_num.append(num)
                    num = []
                k += 1
            max_val = min_val = sum(split_num[0])
            for num in split_num:
                if min_val > sum(num):
                    min_val = sum(num)
                if max_val < sum(num):
                    max_val = sum(num)
            ans.append(max_val - min_val)
    print(min(ans))


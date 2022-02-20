import sys
sys.stdin = open('4408.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnts = [0]*(400//2 + 1)
    res = 0
    for _ in range(N):
        pos, return_pos = map(int, input().split())
        if pos < return_pos:
            for i in range((pos+1)//2, (return_pos+1)//2 +1):
                cnts[i] += 1
        else:
            for i in range((return_pos+1)//2, (pos+1)//2+1):
                cnts[i] += 1
    for cnt in cnts:
        if res < cnt:
            res = cnt
    print(f'#{test_case}', res)
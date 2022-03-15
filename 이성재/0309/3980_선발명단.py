import sys; sys.stdin = open('3980.txt')

def choice(idx, sum):
    global max_sum
    if idx == 11:
        if max_sum < sum:
            max_sum = sum
        return
    
    for i in range(11):
        if arr[idx][i] != 0 and visit[i] == 0:
            visit[i] = 1
            choice(idx + 1, sum + arr[idx][i])
            visit[i] = 0

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visit = [0] * 11
    max_sum = 0
    choice(0, 0)
    print(max_sum)
import sys; sys.stdin=open('swea_숫자만들기.txt')

def dfs(k, v):
    if k == N-1:
        global max_v, min_v
        if v > max_v:
            max_v = v
        if v < min_v:
            min_v = v
        return

    for i in range(4):
        if op_idx[i]:
            op_idx[i] -= 1
            dfs(k+1, cal(v, num[k+1],i))
            op_idx[i] += 1

def cal(x,y,i):
    if i == 0:
        return x + y

    elif i == 1:
        return x - y

    elif i == 2:
        return x * y
    else:
        return int(x / y)

# op = ['+','-','*','/']
T = int(input())
for t in range(1,1+T):
    N = int(input())
    op_idx = list(map(int,input().split()))
    num = list(map(int,input().split()))
    max_v = int(-1e9)
    min_v = int(1e9)
    dfs(0,num[0])
    print(f'#{t}',max_v - min_v)


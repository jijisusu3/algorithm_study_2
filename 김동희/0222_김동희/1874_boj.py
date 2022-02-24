import sys; sys.stdin = open('1874_boj.txt')

N = int(input())
arr = [ int(input()) for _ in range(N)]
stack = [ n for n in range(1,N+1)]
result = []

i = 0
top = 0
result.append('+')
while True:
    if arr[i] == stack[top]:

        result.append('-')
        stack.pop()
        i += 1
        if not top:
            top = 0
        else: top -= 1
        if i == len(arr): break
    else:
        top += 1
        if top == len(stack): break
        result.append('+')

if not stack:
    for r in result:
        print(r)
else:
    print('NO')



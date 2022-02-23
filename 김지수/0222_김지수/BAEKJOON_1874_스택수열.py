import sys
N = int(sys.stdin.readline())
stack = []
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

result = []
for i in range(1, N+1):
    if i != lst[0]:
        stack.append(i)
        result.append('+')
    elif i == lst[0]:
        result.append('+')
        result.append('-')
        lst.pop(0)
    while stack and lst and stack[-1] == lst[0]:
        stack.pop()
        lst.pop(0)
        result.append('-')

if stack or lst:
    print('NO')
else:
    for x in result:
        print(x)



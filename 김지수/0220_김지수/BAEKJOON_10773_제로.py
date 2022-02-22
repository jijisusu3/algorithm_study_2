import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    i = int(sys.stdin.readline())
    if i == 0:
        stack.pop(-1)
    else:
        stack.append(i)
print(sum(stack))
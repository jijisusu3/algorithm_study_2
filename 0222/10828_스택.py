import sys
T = int(sys.stdin.readline())

stack = []
for tc in range(T):
    rule = sys.stdin.readline().split()

    if rule[0] == 'push':
        stack.append(rule[1])
    elif rule[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif rule[0] == 'size':
        print(len(stack))
    elif rule[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif rule[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
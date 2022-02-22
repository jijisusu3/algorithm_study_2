import sys; sys.stdin = open('10828.txt')

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    String = sys.stdin.readline().split()

    if String[0] == 'push':
        lst.append(String[1])

    elif String[0] == 'pop':
        if lst:
            print(lst.pop())

        else:
            print(-1)

    elif String[0] == 'size':
        print(len(lst))

    elif String[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)

    elif String[0] == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)

# 시간 초과....
# N = int(sys.stdin.readline()) / String = sys.stdin.readline().split()
# 변경하면 런타임 에러 (NameError)가 뜬다...
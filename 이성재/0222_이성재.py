# 10828_스택

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


# 10773_제로

import sys; sys.stdin = open('10773.txt')

T = int(input())

stack = []
for tc in range(T):
    N = int(input())

    if N == 0:
        stack.pop()
    else:
        stack.append(N)

sum_a = 0
for i in stack:
    sum_a += i
print(sum_a)


# 1874_스택수열

import sys;

sys.stdin = open('1874.txt')

n = int(input())

stack = []
cnt = 0
flag = True
result = []
for i in range(n):
    m = int(input())

    while cnt < m:
        cnt += 1
        stack.append(cnt)
        result.append('+')

    if stack[-1] == m:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if flag == False:
    print('NO')
else:
    for i in result:
        print(i)


# 17298_오큰수

import sys; sys.stdin = open('17298.txt')

N = int(input())
arr = list(map(int, input().split()))

stack = []
result = [-1] * N

for i in range(N):
    while len(stack) != 0 and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)
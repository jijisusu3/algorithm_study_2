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
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
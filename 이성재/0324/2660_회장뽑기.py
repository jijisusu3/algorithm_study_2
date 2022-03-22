import sys; sys.stdin = open('123.txt')

N = int(input())
arr = [[] for _ in range(N + 1)]
while arr:
    a, b = map(int, input().split())
    if a == -1:
        break
    arr[a].append(b)
    arr[b].append(a)

result = [[0] * (N + 1) for _ in range(N + 1)]
print(result)
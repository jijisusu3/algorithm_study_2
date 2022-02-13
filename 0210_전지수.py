# 3321 못풀었다.

# 1543
# 슬라이싱 말고 방법이 있을까...
w = input()
a = input()

cnt = 0
i = 0

while i <= len(w) - len(a):
    if w[i:i + len(a)] == a:
        cnt += 1
        i += len(a)
    else:
        i += 1

print(cnt)

# 1427

num = list(map(int, input()))

n = len(num)

for i in range(n-1, -1, -1):
    for j in range(0, n-1):
        if num[i] < num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]

for h in num:
    print(h, end='')

#10989

#이렇게 하면 시간초과
N = int(input())

num = [0] * 10001

for i in range(N):
    num[int(input())] += 1

for h in range(10001):
    cnt = num[h]
    for j in range(cnt):
        print(h)

#바꿨더니 pass
import sys

N = int(sys.stdin.readline())

num = [0] * 10001

for i in range(N):
    n = int(sys.stdin.readline())
    num[n] += 1

for h in range(10001):
    cnt = num[h]
    for j in range(cnt):
        print(h)
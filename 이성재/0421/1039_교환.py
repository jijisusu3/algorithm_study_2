import sys; sys.stdin = open('123.txt')

N, K = input().split()
q = set()
k = int(K)

q.add((N, k))
answer = -1
while q:
    a, k = q.pop()

    if k == 0:
        if answer < int(a):
            answer = int(a)
        continue
        
    k -= 1

    for i in range(len(N)):
        for j in range(i, len(N)):
            arr = list(a)
            arr[i], arr[j] = arr[j], arr[i]
            s = ''.join(arr)

            if s[0] == '0':
                continue

            q.add((s, k))

print(answer)



# N, K = input().split()

K = int(K)
arr = [[0] * 11 for _ in range(1000001)]  # K가 10 이하 N이 백만 이하
arr[0] = 1
t = []
for i in N:
    t.append(i)
q = []
q.append([t, 0])

def switch(n, a, b):
    oo = n[a]
    n[a] = n[b]
    n[b] = oo

answer = -1
while q:
    n, k = q.pop(0)

    if k == K:
        answer = max(answer, int(''.join(n)))
        continue

    for i in range(len(N)):
        for j in range(i + 1, len(N)):
            if i == 0 and n[j] == '0':
                continue
            switch(n, i, j)
            m = int(''.join(n))
            if arr[m][k + 1] == 0:
                arr[m][k + 1] = 1
                q.append([n[:], k + 1])
            switch(n, i, j)
print(answer)
import sys;

sys.stdin = open('2309.txt')
N = 9
lst = []  # lst = [20, 7, 23, 19, 10, 15, 25, 8, 13]
for i in range(N):
    lst.append(int(sys.stdin.readline()))

# 난쟁이 키의 합 구하기

total = 0
for i in lst:
    total += i  # total = 140

# 총 합에서 2가지 인자를 뺐을 때 100이 나오는 상황

a = 0
b = 0
for i in lst:
    for j in lst:
        if total - i - j == 100:
            a = i
            b = j

'''
a = 0
b = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if total - lst[i] - lst[j] == 100:
            a = lst[i]
            b = lst[j]

'''

lst.remove(a)
lst.remove(b)  # lst = [20, 7, 23, 19, 10, 8, 13]

# 오름차순으로 정렬
for i in range(len(lst) - 1, -1, -1):
    for j in range(0, i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

for i in lst:
    print(i)


# 순열함수를 구현하고
# if를 사용해서 마지막 값을 나타낼 땐 -1, 마지막 값이 아닐 땐 2번째 값을 도출하도록 한다.
# 풀이실패...

import sys; sys.stdin = open('10972.txt')

N = int(input())
A = list(map(int, input().split()))
visited = [0]*N  # 데이터의 사용 여부 - 데이터의 index 기록 ex)visited[1]=1
arr = [0]*N  # 어떤 데이터를 선택했는가 (순열 정보 저장) ex)arr[1]=2


'''
def perm(level):
    if level >= N:
        print(arr)
        return

    for i in range(N):
        if visited[i] == 1:continue
        visited[i] = 1  # 사용표시(i인덱스에 있는 데이터 사용 중)
        arr[level] = A[i]
        perm(level+1)
        visited[i] = 0 # 사용해제

for i in perm(0):
    if A == [i][-1]:
        print(-1)

else:
    print([i][1])
'''


import sys ; sys.stdin = open('9095.txt')

T = int(input())

# 규칙을 찾고 함수로 만들기!

def a(T):
    if T == 1:
        return 1
    if T == 2:
        return 2
    if T == 3:
        return 4
    else:
        return a(T-1) + a(T-2) + a(T-3)


for i in range(T):
    result = int(input())
    print(a(result))

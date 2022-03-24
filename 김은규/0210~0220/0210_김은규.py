# 1427_백준

a = list(map(int, input()))  # input 값을 int로 변환하고 list a 에 저장.
N = len(a)
for j in range(N-1, -1, -1):  # 뒤에서부터 처음까지 -1씩 작아지면서 반복
    for i in range(0, N-1):  # 0부터 N-2 의 위치값까지 비교해야 하기 때문에 N-2+1
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]  # 내림차순으로 변경


for k in a:  # 리스트 값을 k로 도출.
    print(k, end="")  # k를 줄바꿈없이 한 줄로 출력



# 1543_백준

'''
while len(word) < len(text):
    if text[0:len(word)] == word:
        cnt += 1
        for i in text:
            a = list(i)
        for j in word:
            b = list(j)
        c = a - b
        text = map(str, c)

        실패...
'''

text = input()
word = input()
cnt = 0
i = 0
while len(text) - len(word) >= i:
    if text[i:i+len(word)] == word:
        cnt += 1
        i += len(word)  # 단어의 길이만큼 인덱스에 더해주기 -> 해당 부분 이후부터 if문 수행
    else:
        i += 1 # 찾지 못하면 1만큼 인덱스를 더하고 다시 if문 수행

print(cnt)


# 10989 백준 메모리 초과

import sys
N = int(sys.stdin.readline()) # N = 10
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))  # lst = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]
max_v = 0
for i in lst:
    if i > max_v:
        max_v = i
B = [0] * (max_v+1)
C = [0] * (len(lst))

for val in lst: # 카운팅
    B[val] += 1

for i in range(1, max_v+1): # 누적
    B[i] = B[i-1] + B[i]

for i in range(len(lst)-1, -1, -1):
    B[lst[i]] -= 1
    C[B[lst[i]]] = lst[i]

for i in C:
    print(i)


# 3321 codeup 실패,,,

N = int(input()) # 토핑 종류
A, B = map(int, input().split()) # A : 도우가격 B : 토핑가격
d_kal = int(input()) # 도우 칼로리
t_kay = []
for i in range(N):
    t_kay.append(int(input()))

# 도우만 있을 때 가격
dp = d_kal / A

# 토핑추가
for i in t_kay:
    A






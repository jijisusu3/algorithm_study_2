# 2309

import sys
sys.stdin = open('2309.txt')

N = [int(input()) for h in range(9)] # 입력을 리스트로 변환
# print(N) = [7, 8, 10, 13, 15, 19, 20, 23, 25] N에 정상적으로 저장된 것 확인

total = 0 # 합을 만들어줌
for h in N:
    total += h
print(total)

for i in range(9):
     for j in range(9):
        if total - N[i] - N[j] == 100: #
            for k in range(9):
                if k == i or k == j:
                    # 이 다음 과정에서 원하는 답 도출 실패

#10972

N = int(input())
arr = list(map(int, input().split()))

# 뒤에서부터 시작 해 뒤의 값이 앞의 값보다 크면 바꾸기
for i in range(N - 1, 0, -1):
    if arr[i] < arr[i - 1]:
        for j in range(N - 1, 0, -1):
# 도출 실패

# 9095

import sys

sys.stdin = open('2309.txt')

N = int(input())


def s(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return s(num - 1) + s(num - 2) + s(num - 3)


for i in range(N):
    n = int(input())
    print(s(n))
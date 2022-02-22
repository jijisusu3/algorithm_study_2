import sys; sys.stdin = open('10773.txt', 'r')

K = int(input())  # K = 4
lst = []  # append, pop 위한 리스트 생성
result = 0  # 결과값 초기화
for i in range(K):
    num = int(input())  # 입력값 3 0 4 0
    if num > 0:
        lst.append(num)
        result += num
    else:  # num = 0 경우
        result -= lst[-1]
        lst.pop()

print(result)




import sys; sys.stdin = open('1874.txt', 'r')

n = int(input())
stack = []
result = []
Flag = True  # 불가능한 경우 빠져나가기 위해 Flag 설정
i = 0
for _ in range(n):  # 1~n 오름차순으로 입력
    num = int(input())  # 입력받는 숫자 4 3 6 8 7 5 2 1
    while i < num:
        i += 1
        stack.append(i)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')

    else:
        Flag = False

if Flag:
    for i in result:
        print(i)

else:
    print('NO')


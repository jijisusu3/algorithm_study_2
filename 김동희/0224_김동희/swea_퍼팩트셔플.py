import sys; sys.stdin=open('swea_퍼팩트셔플.txt')

TC = int(input())
for tc in range(1,1+TC):
    N = int(input())
    arr = list(input().split())

    stack1 = []
    stack2 = []
    # 반은 stack1
    while ((N+1)//2):
        stack1.append(arr.pop(0))
        N -= 2
    # 나머지 stack2
    while arr:
        stack2.append(arr.pop(0))
    # stack1이 더 긴 경우 밖에 없으므로
    while stack1:
        arr.append(stack1.pop(0))

        # if stack2: # stack 2가 짧으면 실행 안함.
        if stack2:
            arr.append(stack2.pop(0))

    print(f'#{tc}',*arr)
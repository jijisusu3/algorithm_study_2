def solution(expression):
    answer = []
    op_list = [0,0,0]
    number = []

    num = ''
    for e in expression:
        if e == "+": op_list[0] += 1; number.append(int(num)); num = ''
        elif e == "-": op_list[1] += 1; number.append(int(num)); num = ''
        elif e == "*": op_list[2] += 1; number.append(int(num)); num = ''
        else: num += e;
    number.append(int(num))
    N = len(number)
    print(op_list, number)

    max_v = int(-1e9)
    min_v = int(1e9)

    # def dfs(k, v):
    #     if k == N - 1:
    #         nonlocal max_v, min_v
    #         if v > max_v:
    #             max_v = v
    #         if v < min_v:
    #             min_v = v
    #         return
    #
    #     for i in range(3):
    #         if op_list[i]:
    #             op_list[i] -= 1
    #             dfs(k + 1, cal(v, number[k + 1], i))
    #             op_list[i] += 1
    #
    # def cal(x, y, i):
    #     if i == 0:
    #         return x + y
    #
    #     elif i == 1:
    #         return x - y
    #
    #     elif i == 2:
    #         return x * y
    #
    # dfs(0, number[0])
    # print(max_v,min_v)
    #
    #
    # return answer

asdfjkl = solution("100-200*300-500+20")


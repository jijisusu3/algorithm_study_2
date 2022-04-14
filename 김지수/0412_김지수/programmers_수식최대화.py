expression = "100-200*300-500+20"
# expression = list(expression)
# cal = []
# x = 0
# for i in range(len(expression)):
#     if expression[i] in '*+-':
#         temp_num = expression[x:i]
#         temp_cal = expression[i]
#         y = ''
#         for j in temp_num:
#             y += str(j)
#         cal.append(int(y))
#         cal.append(temp_cal)
#         x = i + 1
# temp_num = expression[x:len(expression)+1]
# y = ''
# for j in temp_num:
#     y += str(j)
# cal.append(int(y))

# ============이제야 리스트에 담음============

priors = [
    {'*': 1, '+': 2, '-': 3}, {'*': 1, '-': 2, '+': 3},
    {'+': 1, '-': 2, '*': 3}, {'+': 1, '*': 2, '-': 3},
    {'-': 1, '*': 2, '+': 3}, {'-': 1, '+': 2, '*': 3}
]

result = []
for prior in priors:
    box = []
    stack = []
    for token in expression:
        if type(token) == int:
            box.append(token)
        else:
            while stack and prior[token] <= prior[stack[-1]]:
                box.append(stack.pop())
            stack.append(token)

    while stack:
        box.append(stack.pop())

    for i in box:
        if i in prior:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
    result.append(stack[0])

print(result)



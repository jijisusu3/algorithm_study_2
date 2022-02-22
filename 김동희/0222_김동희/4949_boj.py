def check_func(s):
    check = []
    top = -1
    for i in s:
        if i == '(' or i == '[':
            check.append(i)
            top += 1
        elif i == ')' or i == ']':
            if top == -1:
                return 'no'
            elif i == ')':
                if check[top] == '(':
                    check.pop()
                    top -= 1
                else:
                    return 'no'
            elif i == ']':
                if check[top] == '[':
                    check.pop()
                    top -= 1
                else:
                    return 'no'

    if check:
        return 'no'
    else:
        return 'yes'

s = input()
while s != '.':
    print(check_func(s))
    s = input()

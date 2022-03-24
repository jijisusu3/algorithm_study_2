def solution(s):
    n = len(s)
    result = ''
    string = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8' , 'nine':'9'}
    temp = ''
    for i in range(n):
        if s[i] in '0123456789':
            result += s[i]
        else:
            temp += s[i]
        for j in string:
            if j == temp:
                result += string[j]
                temp = ''
    return int(result)




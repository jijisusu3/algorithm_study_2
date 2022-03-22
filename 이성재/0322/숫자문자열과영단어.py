def solution(s):
    answer = ''
    alp = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    alpha = ''
    for i in s:
        if i in '0123456789':
            answer += i
        else:
            alpha += i
        if alpha in alp.keys():
            answer += alp[alpha]
            alpha = ''

    return int(answer)
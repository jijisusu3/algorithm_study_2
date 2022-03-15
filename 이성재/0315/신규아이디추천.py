def solution(new_id):
    ans = ''

    new_id = new_id.lower()

    id = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    for i in new_id:
        if i in id:
            ans += i

    answer = ans[0]
    for i in ans[1:]:
        if i != '.':
            answer += i
        elif i == '.' and answer[-1] != '.':
            answer += i

    if answer[0] == answer[-1] == '.':
        answer = answer[1:-1]
    elif answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]

    if answer == '':
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) == 1:
        answer = answer * 3
    elif len(answer) == 2:
        answer += answer[-1]

    return answer

print(solution('=.='))
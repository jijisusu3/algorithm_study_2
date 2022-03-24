def solution(s):
    '''
    문: 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임
    "one4seveneight"
    풀이 : 탐색, 하나씩 담는다. 숫자면 그냥 넣고 문자면 체크리스트에담아 체크한후,
    '''
    answer = ''
    check_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    check = ''

    for i in s:
        if i.isdigit():
            answer += i
        else:
            check += i
            if check in check_list:
                ans = find_s(check)
                answer += str(ans)
                check = ''

    return int(answer)

def find_s(s):
    check_dic = {'zero': 0,
                 'one': 1,
                 'two': 2,
                 'three': 3,
                 'four': 4,
                 'five': 5,
                 'six': 6,
                 'seven': 7,
                 'eight': 8,
                 'nine': 9}
    return check_dic[s]
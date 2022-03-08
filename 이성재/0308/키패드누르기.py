def solution(numbers, hand):
    l_hand = '*'
    r_hand = '#'
    answer = ''
    dict_a = {1 : (0,0), 2 : (0,1), 3 : (0,2), 4 : (1,0), 5 : (1,1), 6 : (1,2), 7 : (2,0), 8 : (2,1), 9 : (2,2), '*' : (3,0), 0 : (3,1), '#' : (3,2)}
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l_hand = i
        elif i in [3, 6, 9]:
            answer += 'R'
            r_hand = i
        else:
            l_dis = abs(dict_a[i][0] - dict_a[l_hand][0]) + abs(dict_a[i][1] - dict_a[l_hand][1])
            r_dis = abs(dict_a[i][0] - dict_a[r_hand][0]) + abs(dict_a[i][1] - dict_a[r_hand][1])

            if l_dis < r_dis:
                answer += 'L'
                l_hand = i
            elif l_dis > r_dis:
                answer += 'R'
                r_hand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    l_hand = i
                else:
                    answer += 'R'
                    r_hand = i

    return answer
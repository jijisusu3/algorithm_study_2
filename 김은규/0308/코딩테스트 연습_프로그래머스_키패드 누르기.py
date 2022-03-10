def solution(numbers, hand):
    answer = ''
    lst = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left = [3, 0]
    right = [3, 2]
    for i in numbers:
        if i in [1, 4, 7]:  # 왼쪽
            answer += 'L'
            left = lst[i]

        elif i in [3, 6, 9]:  # 오른쪽
            answer += 'R'
            right = lst[i]

        else:  # 가운데
            left_d = abs(lst[i][0] - left[0]) + abs(lst[i][1] - left[1])
            right_d = abs(lst[i][0] - right[0]) + abs(lst[i][1] - right[1])

            if left_d == right_d:
                if hand == 'right':
                    answer += 'R'
                    right = lst[i]

                else:
                    answer += 'L'
                    left = lst[i]

            elif left_d > right_d:
                answer += 'R'
                right = lst[i]

            else:
                answer += 'L'
                left = lst[i]

    return answer

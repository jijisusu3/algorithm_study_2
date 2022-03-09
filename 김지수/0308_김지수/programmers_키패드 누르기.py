def solution(numbers, hand):
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_r, left_c = 3, 0
    right_r, right_c = 3, 2
    len_num = len(numbers)

    for i in range(len_num):
        for r in range(4):
            for c in range(3):
                if numbers[i] == phone[r][c]:
                    numbers[i] = [r, c]

    result = ''
    for row, col in numbers:
        if col == 0:
            result += 'L'
            left_r, left_c = row, col
        elif col == 2:
            result += 'R'
            right_r, right_c = row, col

        else:
            left_go = abs(row-left_r) + abs(col-left_c)
            right_go = abs(row-right_r) + abs(col-right_c)
            if left_go == right_go:
                if hand == 'right':
                    right_r, right_c = row, col
                    result += 'R'
                else:
                    left_r, left_c = row, col
                    result += 'L'
            elif left_go > right_go:
                right_r, right_c = row, col
                result += 'R'
            else:
                left_r, left_c = row, col
                result += 'L'
    return result
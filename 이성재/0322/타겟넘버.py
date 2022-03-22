def solution(numbers, target):
    tree = [0]
    for i in numbers:
        L = []
        R = []
        for j in tree:
            L.append(j + i)
            R.append(j - i)
        tree = L + R

    answer = 0
    for i in tree:
        if i == target:
            answer += 1
    return answer
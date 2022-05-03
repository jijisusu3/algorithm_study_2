s = 'baabaa'

def solution(s):
    answer = 0

    arr = []
    for i in s:
        if len(arr) == 0:
            arr.append(i)
        elif arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)

    if len(arr) == 0:
        answer = 1

    return answer

print(solution(s))
def solution(array, commands):
    answer = []
    for d in commands:
        a = d[0]
        b = d[1]
        c = d[2]
        arr = []
        for i in range(a-1,b):
            arr.append(array[i])
        arr = sorted(arr)
        answer.append(arr[c-1])
    return answer
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
#[5, 6, 3]
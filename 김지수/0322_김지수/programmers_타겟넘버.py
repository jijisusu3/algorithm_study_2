def solution(numbers, target):
    answer = 0

    def dfs(k, result):
        if k == n:
            if result == target:
                nonlocal answer
                answer += 1
                return
        else:
            dfs(k + 1, result + numbers[k])
            dfs(k + 1, result - numbers[k])

    n = len(numbers)
    dfs(0, 0)
    return answer
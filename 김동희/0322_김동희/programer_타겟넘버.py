def solution(numbers, target):
    '''
    문제 : 타겟 넘버를 만드는 방법의 수
    풀이 : 더하고 뺸다. dfs의 포함하고 포함하지 않는다.
    '''
    answer = 0

    def dfs(i, ssum, n, t):
        '''
        i=늘어나는 수, ssum = 초기값 0, n=list,t = target
        '''
        nonlocal answer
        if i == len(n):
            if ssum == t:
                answer += 1
                return
            return

        dfs(i + 1, ssum + n[i], n, t)
        dfs(i + 1, ssum - n[i], n, t)

    dfs(0, 0, numbers, target)
    return answer
def solution(progresses, speeds):
    answer = []
    done = 0
    time = 1
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            done += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            time += 1
            if done > 0:
                answer.append(done)
                done = 0
    answer.append(done)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))

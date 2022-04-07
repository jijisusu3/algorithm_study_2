def solution(progresses, speeds):

    # 몇일 필요한가.
    day = []
    i = 0
    for n in progresses:
        d_cnt = 0
        while n < 100:
            n += speeds[i]
            d_cnt += 1
        day.append(d_cnt)
        i += 1

    # 빼서 비교한 후 크면 += 1 [5, 10, 1, 1, 20, 1]
    answer = []
    while day:
        j = day.pop(0)
        cnt = 1
        while day and j >= day[0]:
            day.pop(0)
            cnt += 1
        answer.append(cnt)

    return answer

ans = solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
print(ans)

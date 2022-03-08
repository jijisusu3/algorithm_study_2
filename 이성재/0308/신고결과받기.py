def solution(id_list, report, k):
    list_re = [[] for _ in range(len(id_list))]
    list_id = [0] * len(id_list)
    report = set(report)
    for j in range(len(id_list)):
        for i in report:
            a, b = i.split(' ')
            if id_list[j] == a:
                list_re[j].append(b)
            if id_list[j] == b:
                list_id[j] += 1

    list_stop = []
    for i in range(len(id_list)):
        if list_id[i] >= k:
            list_stop.append(id_list[i])

    answer = [0] * len(id_list)
    for j in range(len(list_re)):
        for k in list_re[j]:
            if k in list_stop:
                answer[j] += 1
    return answer
from collections import deque


def solution(n, info):
    Q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    result = []
    gap_max = 0

    while Q:
        shoot, lst = Q.popleft()

        if sum(lst) == n:  # 화살 다 쏨
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and lst[i] == 0):
                    if info[i] >= lst[i]:  # 어피치 win
                        apeach += 10 - i
                    else:  # 라이언 win
                        lion += 10 - i
            if lion > apeach:
                gap = lion - apeach
                if gap < gap_max: continue
                if gap > gap_max:
                    gap_max = gap
                    result = []
                result.append(lst)

        elif sum(lst) > n:
            continue

        elif shoot == 10:
            temp = lst.copy()
            temp[shoot] = n - sum(temp)
            Q.append((-1, temp))

        else:
            temp1 = lst.copy()
            temp1[shoot] = info[shoot] + 1
            Q.append((shoot + 1, temp1))

            temp2 = lst.copy()
            temp2[shoot] = 0
            Q.append((shoot + 1, temp2))

    if not result:
        return [-1]
    elif len(result) == 1:
        return result[0]
    else:
        return result[-1]


print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))


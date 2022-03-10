# 머리가 멈췄다.... 풀다가 결국 다른 사람 풀이 참조...

def solution(id_list, report, k):
    answer = [0]*len(id_list)  # 결과값으로 id_list의 인자가 메일을 받는 개수를 도출하기 위해 id_list의 숫자만큼 list의 값 0으로 설정.

    dic = {i : [] for i in id_list}  # dic:  {'muzi': [], 'frodo': [], 'apeach': [], 'neo': []}
                                     # id_list의 값을 key로 하는 딕셔너리 생성.

    for report_set in set(report): # 중복 제거하고 저장
        report_set = report_set.split()
        dic[report_set[1]].append(report_set[0])  # 신고 당한 사람 key, 신고 한 사람 value 값으로 저장.
                                                  # dic: {'muzi': ['apeach'], 'frodo': ['muzi', 'apeach'], 'apeach': [], 'neo': ['frodo', 'muzi']}


    for key, value in dic.items():
        if len(value) >= k:  # 신고한 사람의 숫자가 k 이상일 경우 그 숫자만큼 메일을 받게 됨.
            for v in value:  # 해당 value 가 신고한 사람들이고, 그들은 메일을 받게 되기 때문에
                answer[id_list.index(v)] += 1  # answer의 인덱스 값으로 활용해서 1씩 증가시켜 준다.

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))



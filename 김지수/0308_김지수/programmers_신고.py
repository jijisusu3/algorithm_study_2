id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"]
k = 2
id_len = len(id_list)
report = set(report)
report = list(report)

dic = {}

for name in id_list:
    dic[name] = {
        'complain': [],
        'num': 0,
    }

ban = []

for i in report:
    good, bad = i.split()
    dic[good]['complain'].append(bad) # 신고자에게 신고한 사람 기록
    dic[bad]['num'] += 1
    if dic[bad]["num"] == k:
        ban.append(bad)

letter = [0]*id_len
idx = 0
for x in id_list:
    for y in ban:
        if y in dic[x]['complain']:
            letter[idx] += 1
    idx += 1

print(letter)

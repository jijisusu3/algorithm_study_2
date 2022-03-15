def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    N = len(new_id)
    except_char = '~!@#$%^&*()=+[{]}:?,<>/'
    except_lst = []
    for i in range(N):
        if new_id[i] in except_char:
            except_lst.append(i)
    copy_id = ''
    for i in range(N):
        if i in except_lst: continue
        copy_id += new_id[i]
    N = len(copy_id)
    copy_id = list(copy_id)
    i = 0
    ans = []
    while i < N:
        if copy_id[i] != '.':
            ans.append(copy_id[i])
            i += 1
        else:
            cnt = 0
            while i + cnt < N and copy_id[i + cnt] == '.':
                cnt += 1
            i += cnt
            ans.append('.')
    if ans[0] == '.':
        ans.pop(0)
    if len(ans) > 0:
        if ans[-1] == '.':
            ans.pop()
    if len(ans) == 0:
        ans += ['a']
    if len(ans) >= 16:
        while len(ans) > 15:
            ans.pop()
        if ans[-1] == '.':
            ans.pop()
    if len(ans) <= 2:
        while len(ans) < 3:
            ans += ans[-1]
    for a in ans:
        answer += a
    return answer

new_id = "=.="
print(solution(new_id))

# 시간초과

# def solution(s):
#     s = list(s)
#     s_len = int(len(s)/2)
#     while s_len > 0:
#         for i in range(len(s)-1):
#             if s[i] == s[i+1]:
#                 if i == 0:
#                     s = s[i+2:]
#                     break
#                 elif i == len(s) - 2:
#                     s = s[:i]
#                     break
#                 else:
#                     s = s[:i] + s[i + 2:]
#                     break
#         s_len -= 1
#     if s:
#         return 0
#     else:
#         return 1


def solution(s):
    Q = []
    for i in s:
        if len(Q) == 0:
            Q.append(i)
            continue
        if Q[-1] == i:
            Q.pop()
        else:
            Q.append(i)
    if Q:
        return 0
    else:
        return 1


# 아이디어
# 2차원 배열의 각 좌표를 시작점으로 DFS 실행
# 만들 수 있는 6자리의 모든 조합 list 에 저장
# set 를 활용하여 중복 제거 후 len 으로 개수 출력
# 실패
# 문자로 저장

import sys; sys.stdin = open('2210.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def DFS(r, c, word):
    word += arr[r][c]

    if len(word) == 6:
        tmp.append(word)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            DFS(nr, nc, word)

tmp = []
arr = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(5):
        word = ''
        DFS(i, j, word)

result = len(list(set(tmp)))
print(result)
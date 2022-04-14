# 내가 짠 코드....시간초과................................

from collections import deque
import sys

d = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
H, W = map(int, input().split())  # 가로세로
arr = [list(sys.stdin.readline().rstrip()) for i in range(H)]
Q = deque()
temp = deque()

'''
while문이 돌아가려면 temp에 하나라도 들어가 잇어야 하니까
어차피 '.'으로 바꾸니까 바뀌어도 상관없는 '.'을 찾아서
나중에 '.'으로 하나 바꿔줌, 만약 '.'이 하나도 없다면
이미 모래성이 변하지 않는 것이므로 그냥 바로 result 출력해도 됨 
최악의 경우 1로 모두 구성되었다고 해도 주변에 모래성이 쌓여있지 않은 부분이
0개이므로, 무너지지않기 때문
'''
flag = True
for r in range(H):
    for c in range(W):
        if arr[r][c] == '.':
            temp.append((r, c))
            flag = False
            break
    if flag == False:
        break


result = 0

# 한 번에 넣어놨다가 처리해야 함. 불 문제 처럼!!!

while temp:
    result += 1
    while temp:
        r, c = temp.popleft()
        arr[r][c] = '.'

    for r in range(H):
        for c in range(W):
            if arr[r][c] != '.':
                Q.append((r, c))
    while Q:
        row, col = Q.popleft()
        cnt = 0
        for i in range(8):
            nr, nc = row + d[i][0], col + d[i][1]
            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == '.':
                    cnt += 1
        if cnt >= int(arr[row][col]): # 모래성이 쌓여있지 않은 부분의 개수가 자기 모래성의 튼튼함보다 많거나 같을 때
            temp.append((row, col)) # 다음 회차때 '.'으로 변경될 애들 담아두기

print(result)
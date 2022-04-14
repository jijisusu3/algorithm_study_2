places = [["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]
result = []

dr1 = [-1, 1, 0, 0]
dc1 = [0, 0, -1, 1]
dr2 = [-1, -1, 1, 1]
dc2 = [-1, 1, -1, 1]


def keep_distance(row, col):
    temp = []
    for i in range(4): # 상하좌우 확인해보고 사람 없는지 확인, 파티션 있으면 temp에 담아둠
        nr1, nc1 = row + dr1[i], col + dc1[i]
        if 0 <= nr1 < 5 and 0 <= nc1 < 5:
            if place[nr1][nc1] == 'P':
                return 0  # 상하좌우에 사람 있으면 그냥 여기서 끝
            elif place[nr1][nc1] == 'X':
                temp.append((nr1, nc1))  # 파티션 있으면 담아둠
            else: # 빈 책상인 경우
                go_r, go_c = nr1 + dr1[i], nc1 + dc1[i]  # 그 방향으로 한번 더 가봄
                if 0 <= go_r < 5 and 0 <= go_c < 5 and place[go_r][go_c] == 'P':
                    return 0

    for j in range(4):
        nr2, nc2 = row + dr2[j], col + dc2[j]
        if 0 <= nr2 < 5 and 0 <= nc2 < 5:
            if place[nr2][nc2] == 'P':  # 대각선에 사람 있으면
                cnt = 0
                for x in range(4):
                    temp_r, temp_c = nr2 + dr1[x], nc2 + dc1[x]
                    if (temp_r, temp_c) in temp:
                        cnt += 1
                if cnt < 2 :
                    return 0
    return 1


for place in places:
    flag1 = True
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                temp_result = keep_distance(r, c)
                if temp_result == 0:
                    result.append(0)
                    flag1 = False
                    break
        if flag1 == False:
            break
    if flag1 == True:
        result.append(1)
print(result)







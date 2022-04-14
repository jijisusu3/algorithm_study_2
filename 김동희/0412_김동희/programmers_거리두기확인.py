def solution(places):
    answer = []
    for each_list in places:
        r = 0
        arr = [] # P배열 좌표
        for list_i in each_list:
            c = 0
            for i in list_i:
                if i == 'P':
                    arr.append((r,c))
                c+= 1
            r += 1

        def check():
            S = arr
            while S:
                sr, sc = S.pop()

                # 바로 상하좌우에 있으면 0
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = sr + dr, sc + dc
                    if 0<=nr<5 and 0<=nc<5 and each_list[nr][nc]=="P":
                        return 0
                # 상하좌우 한칸 더 앞에 있고, 파티션 없으면 0
                for dr, dc in ((-2, 0), (2, 0), (0, -2), (0, 2)):
                    nr, nc = sr + dr, sc + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and each_list[nr][nc]=="P":
                        if dr == -2 and each_list[nr + 1][nc] == "X":
                            continue
                        elif dr == 2 and each_list[nr - 1][nc] == "X":
                            continue
                        elif dc == -2 and each_list[nr][nc + 1] == "X":
                            continue
                        elif dc == 2 and each_list[nr][nc - 1] == "X":
                            continue
                        else:
                            return 0

                # 대각선.
                for dr, dc in ((-1,1),(1,1),(1,-1),(-1,-1)):
                    nr, nc = sr + dr, sr + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and each_list[nr][nc]=="P":
                        if dr == -1 and dc == 1 and each_list[nr + 1][nc] =="X" and each_list[nr][nc - 1] =="X":
                            continue
                        elif dr == 1 and dc == 1 and each_list[nr - 1][nc] =="X" and each_list[nr][nc - 1] =="X":
                            continue
                        elif dr == 1 and dc == -1 and each_list[nr - 1][nc] =="X" and each_list[nr][nc + 1] =="X":
                            continue
                        elif dr == -1 and dc == -1 and each_list[nr + 1][nc] =="X" and each_list[nr][nc + 1] =="X":
                            continue
                        else:
                            return 0
            return 1

        ans = check()
        answer.append(ans)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
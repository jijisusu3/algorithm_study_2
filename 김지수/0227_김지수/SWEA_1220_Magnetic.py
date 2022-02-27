import sys; sys.stdin = open('1220.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    # 일단 나갈 수 있는 애들 빼자
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '1':
                for x in range(r+1, N):
                    if arr[x][c] == '2':
                        break
                else:
                    arr[r][c] = '0'
            elif arr[r][c] == '2':
                for y in range(0, r):
                    if arr[y][c] == '1':
                        break
                else:
                    arr[r][c] = '0'
    state = []
    for col in range(N):
        temp = ''
        for row in range(N):
            if arr[row][col] == '1':
                temp += 'N'
            elif arr[row][col] == '2':
                temp += 'S'
        state.append(temp)

    cnt = 0
    for k in state:
        cnt += k.count('NS')
    print(f'#{tc} {cnt}')






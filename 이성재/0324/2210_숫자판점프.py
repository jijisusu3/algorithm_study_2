import sys; sys.stdin = open('123.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y ,num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    
    for i in range(4):
        r = x + dx[i]
        c = y + dy[i]

        if 0 <= r < 5 and 0 <= c < 5:
            dfs(r, c, num + arr[r][c])

arr = [list(map(str, input().split())) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])

print(len(result))
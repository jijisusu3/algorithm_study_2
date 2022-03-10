TC = int(input())


def dfs(start_row, now_sum):
    global add_power
    if start_row == 11:
        if now_sum > add_power:
            add_power = now_sum
        return
    for col in range(11):
        if arr[start_row][col] != 0 and visited[col] == 0:
            visited[col] = 1
            dfs(start_row + 1, (now_sum + arr[start_row][col]))
            visited[col] = 0


for tc in range(TC):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [0]*11

    add_power = 0
    dfs(0, 0)
    print(add_power)



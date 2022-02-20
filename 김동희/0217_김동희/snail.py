N, M = map(int,input().split())
arr =[ [0]*M for _ in range(N)]
# print(arr)
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
n = N*M
r=c=0
while n > 0:
        arr[r][c] = n
        r += dr[d]
        c += dc[d]
        if r < 0 or c < 0 or r >= N or c >= M or arr[r][c] != 0:
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
            n -= 1
        else:
            n -= 1
print(arr)





# code-up(1096) : 바둑판에 흰 돌 놓기

arr = [[0]*19 for _ in range(19)]

N = int(input())
for i in range(N):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
for x in range(19):
    for y in range(19):
        print(arr[x][y], end = ' ')
    print()


# BAEKJOON(10816): 숫자카드
n = int(input())
mine = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

mine.sort()




# BAEKJOON(2805): 나무 자르기

n, m = map(int, input().split())   # n은 나무의 개수 m은 필요한 나무의 양
arr = list(map(int, input().split()))   # 나무의 크기 list

start = 1
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:                              # x가 mid 값 보다 작거나 같을 때는 나무가 안 잘리니까 얘들 빼고
            total += x - mid                     # 잘린 나무 다 더해
    if total >= m:                                # 잘라야 할 것보다 잘릴 나무가 크면!
        start = mid + 1                           # 더 위쪽을 잘라보자
    else:                                        # 그래도 잘라야할 것보다 잘릴 나무 양이 적으면!
        end = mid - 1                            # 더 잘라야 하니까 끝 점을 줄여서 나무가 더 많이 잘리게
print(end)


# while문 안의 if 문과 else문을 바꿔서 썼는데 시간초과 났음 그 이유가 뭘 지..
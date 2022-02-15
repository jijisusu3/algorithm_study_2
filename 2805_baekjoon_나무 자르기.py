import sys; sys.stdin = open('2805.txt')

N, M = list(map(int, input().split()))  # N=나무의 수 M=필요한 나무의 길이
arr = list(map(int, input().split()))  # 나무의 높이

high = 0
for i in arr:
    if i > high:
        high = i  # 끝점 설정을 위해 나무높이 최대값 도출

start = 0  # 시작점 설정
end = high  # 끝점 설정

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2  # 중간값 설정
    for i in arr:
        if i > mid:  # mid 높이로 나무 자르기
            total += i - mid

    #  나무 양이 부족한 경우
    if total < M:
        end = mid - 1

    #  나무 양이 충분한 경우
    else:
        result = mid
        start = mid + 1

print(result)





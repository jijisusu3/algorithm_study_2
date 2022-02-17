n, m = map(int,(input().split()))
array = list(map(int,input().split()))
# 이진 탐색 ! (중간값 활용법)
# 시작 인덱스, 끝 인덱스
start = 0
end = max(array)
result = 0
# 끝 인덱스보다 커지면 그만.
while start <= end:
    # 총 잘린 나무의 총 길이
    total = 0 
    mid = (start + end) // 2
    
    # 각 길이 중에서 중간값보다 크면 자르고, 그 (차이) 길이를 다 더한다.
    for v in array:
        if v > mid:
            total += v - mid
            
    # 총 잘린 나무의 길이가 부족하면 end 설정
    if total < m :
        end = mid -1
    #조건이 최대이므로 저장 결과값 저장
    else:
        result = mid
        start = mid + 1
print(result)


n, m = 4 ,6
array = [19, 15, 10, 17]

# 시작 인덱스, 끝 인덱스
start = 0
end = max(array)

# 이진 탐색 ! (중간값 활용법)
# 결과
result = 0
# 끝 인덱스보다 커지면 그만.
while start < end:
    # 총 잘린 떡의 총 길이
    total = 0 
    # 중간값 추출법
    mid = (start + end) // 2
    
    # 각 길이 중에서
    for v in array:
        # 중간값보다 크면 자르고, 그 (차이) 길이를 다 더한다.
        if v > mid:
            total += v - mid
            
    # 총 잘린 떡의 길이가 부족하면 끝 인덱스를 중간 인덱스보다 1 바로 앞으로 설정.
    if total < m :
        end = mid -1
    # 총 잘린 떡의 길이가 많거나 같으면 (조건이 최대이므로 저장 결과값 저장)
    # 시작 인덱스를 중간 인덱스 보다 1 바로 뒤 설정.
    else:
        result = mid
        start = mid + 1
        
print(result)


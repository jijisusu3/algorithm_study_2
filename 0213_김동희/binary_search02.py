# 이진탐색 반복문
def binary_search(array, target, start, end):
    # 중간점을 활용하는 탐색이라고 볼 수 있고,
    # 시간 복잡도는 O(logN)
    
    #start 시작 인덱스 : 0
    #end 끝 인덱스 : n-1
    if start > end:
        return None
        # 중간 인덱스
    mid = (start+end) // 2
        
    #중간 값이 맞으면 인덱스 추출
    if array[mid] == target:
        return mid
    
    #타겟 값이 중간 값이 크면 끝 인덱스가 중간 인덱스로
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    #타겟 값이 중간 값보다 작으면 시작 인덱스가 중간 인덱스로
    else:
        return binary_search(array, target, mid+1, end)



n, target = 10, 7
array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않는다.')
else:
    print(f'원소가 {result+1}번째 위치합니다.')
        
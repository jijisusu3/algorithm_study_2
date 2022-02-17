import sys; sys.stdin = open('10816.txt')

N = int(input())  # 상근이가 가지고 있는 카드의 개수
arr1 = list(map(int, input().split()))  # 상근이 카드 종류  arr1 = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
M = int(input())  # 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야하는 개수
arr2 = list(map(int, input().split()))  # arr2: [10, 9, -5, 2, 3, 4, 5, -10]


count = {}  # 딕셔너리 생성
for i in arr1:
    if i not in count:
        count[i] = 1  # count 딕셔너리에 값이 없으면 key 값에 i, value 값에 1 추가
    else:
        count[i] += 1  # key 값 존재하면 value 값에 1씩 추가

# count = {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1}

for j in arr2:
    result = count.get(j)  # j가 count 딕셔너리의 key 값에 해당할 때, value 값을 result에 저장.
    if result == None:
        print(0, end=' ')
    else:
        print(result, end=' ')








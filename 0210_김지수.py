
# code-up (3321) : 최고의 피자

topping_num = int(input()) # 토핑의 수
dough_price, topping_price = map(int, input().split()) # 공백으로 나누어서 도우 가격과, 토핑 하나 당 가격 받아오기
dough_calorie = int(input()) # 도우의 칼로리
toppings = [] # 토핑 칼로리들 저장할 빈 리스트
for _ in range(topping_num): # 토핑의 수 만큼
    toppings.append(int(input())) # 토핑의 칼로리를 입력받아, 빈 리스트에 하나하나 채워넣는다. 
toppings.sort(reverse=True) # 칼로리 높은 것 부터 받기 위해 sort(reverse=True)를 통해 내림차순으로 정리한다.

result = 0 # print할 값
t_kcal = 0 # 토핑들의 칼로리를 더할 값
t_cost = 0 # 토핑들의 가격을 더할 값
for i in toppings: # 내림차순으로 정렬된 토핑칼로리 리스트를 돌면서
    t_kcal += i # 토핑 칼로리를 더하고
    t_cost += topping_price # 토핑 가격도 더하고 
    total = (dough_calorie + t_kcal)/(dough_price+t_cost)  #1달러 당 가격
    if result > total: # total이 result보다 1달러당 가격이 작으면
        break # 반복문 멈추기! 왜냐하면 토핑의 값이 같기 때문에, 내림차순이라 뒤에는 더 낮은 가격의 토핑만 있어서 더 더할 수록 손해임
    else:
        result = total # total이 result보다 1달러당 가격이 크면, 그 값을 다음 반복문에서 비교해봐야하니까 result에 넣기
print(int(result))



# BAEKJOON(10989): 수 정렬하기 3

# Bubble Sort -> 백준에서는 메모리 초과 뜸
import sys
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
for i in range(n-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(*lst, sep='\n')

# Counting Sort
import sys
n = int(sys.stdin.readline())
lst = [0]*10001
for _ in range(n):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(1, 10001):
    count = lst[i]
    for _ in range(count):
        print(i)



# BAEKJOON(1427): 소트인사이드

# Counting Sort  -> 백준 사이트에서 안됨... 왜 안되는지 너무 궁금
num = input()
temp_lst = [0]*10
for i in num:
    temp_lst[int(i)] += 1
for j in range(len(temp_lst)-1, 0, -1):
    for _ in range(temp_lst[j]):
        print(int(j), end='')


# 2. 그냥 풀기..

num = input()
for i in range(9, -1, -1):
    for j in num:
        if int(j) == i:
            print(i, end='')



# BAEKJOON(1543): 문서 검색

doc = list(input())
search = list(input())
x = len(doc)-len(search)
y = len(search)
cnt = 0
i = 0
while i <= x:
    if doc[i:i+y] == search:
        cnt += 1
        i += y
    else:
        i += 1
print(cnt)
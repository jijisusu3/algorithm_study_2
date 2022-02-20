# 3321 : 최고의 피자

import sys; sys.stdin = open('3321.txt')

n = int(input())
a,b = map(int,input().split())
c = int(input())
d = []
for i in range(n):
    d.append(int(input()))

## 토핑 칼로리를 내림차순으로
num = 0
for j in range(n):
    for k in range(j, n):
        if d[k] > d[j]:
            num = d[k]
            d[k] = d[j]
            d[j] = num

## 최고의 피자 찾기
cal = c
cost = a
max_cal = 0
for i in d:
    cal = cal + i
    cost = cost + b

    cpc = cal / cost
    if cpc > max_cal:
        max_cal = cpc

## int함수
int_mc = 0
while int_mc < max_cal:
    if 0 <= max_cal - int_mc < 1:
        break
    else:
        int_mc = int_mc + 1

print(int_mc)





# 10989 : 수 정렬하기 3

import sys; sys.stdin = open('10989.txt')

N = int(input())
arr = []
for tc in range(1, N + 1):
    arr.append(int(input()))

for i in range(N):
    for j in range(i, N):
        num = 0
        if arr[i] > arr[j]:
            num = arr[i]
            arr[i] = arr[j]
            arr[j] = num

for i in arr:
    print(i)





# 1427 : 소트인사이드

import sys; sys.stdin = open('1427.txt')

N = input()

len_N = 0
for i in N:
    len_N += 1

d = []
for i in N:
    d.append(i)

for i in range(len_N):
    for j in range(i, len_N):
        if d[i] < d[j]:
            b = d[j]
            d[j] = d[i]
            d[i] = b

for i in d:
    print(i, end="")





# 1543 : 문서 검색

import sys; sys.stdin = open('1543.txt')

a = input()
b = input()

# a, b의 길이
len_a = 0
len_b = 0
for i in a:
    len_a += 1
for i in b:
    len_b += 1

# 슬라이싱..
num = 0
cnt = 0
while num <= len_a - len_b:
    if a[num:num + len_b] == b:
        cnt += 1
        num += len_b
    else:
        num += 1
print(cnt)
# CodeUp_3321
N = int(input())
A, B = map(int, input().split())
C = int(input())
Di = []
for _ in range(N):
    Di.append(int(input()))

for i in range(N):
    for j in range(N-i-1):
        if Di[j] > Di[j+1]:
            Di[j], Di[j+1] = Di[j+1], Di[j]

prices = []
for k in range(0, N+1):
    cal = C
    for i in range(k):
        cal += Di[N-1-i]

    price = A + k*B
    prices.append(cal//price)

max_val = prices[0]
for price in prices:
    if max_val < price:
        max_val = price

print(max_val)

# Baekjoon_1427
nums = list(map(int, input()))
N = len(nums)
for i in range(N):
    for j in range(0, N-i-1):
        if nums[j] <nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
for num in nums:
    print(num, end='')

# Baekjoon_1543
docs = list(input())
word = input()
length = len(word)
cnt = 0
while len(docs) > length-1:
    doc_word = ''
    for i in range(length):
        doc_word += docs[i]
    if word == doc_word:
        cnt += 1
        for _ in range(length):
            docs.pop(0)
    else:
        docs.pop(0)
print(cnt)

# Baekjoon_10989
N = int(input())
cnts = [0]*(10000+1)
for _ in range(N):
    num = int(input())
    cnts[num] += 1

for i in range(10000+1):
    while cnts[i] != 0:
        print(i)
        cnts[i] -= 1
        continue

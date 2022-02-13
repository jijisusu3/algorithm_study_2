# BAEKJOON(2309):일곱 난쟁이
import sys
dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))
num = sum(dwarfs) - 100
breaker = False
for i in range(9):
    for j in range(8, i, -1):
        temp = dwarfs[i]+dwarfs[j]
        if temp == num:
            temp_target1 = dwarfs[i]
            temp_target2 = dwarfs[j]
            dwarfs.remove(temp_target1)
            dwarfs.remove(temp_target2)
            breaker = True
            break
    if breaker == True:
        break
result = sorted(dwarfs)
for dwarf in result:
    print(dwarf)




# BAEKJOON(10972): 다음 순열

import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
for i in range(n-1, 0, -1):
    if data[i-1] <data[i]: # 뒤의 값이 앞 값보다 크면






# BAEKJOON(9095): 1, 2, 3 더하기

import sys
n = int(sys.stdin.readline())


def go(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return go(num-1)+go(num-2)+go(num-3)


for _ in range(n):
    result = int(sys.stdin.readline())
    print(go(result))


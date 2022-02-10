num = input()
lst = [0]*10
for i in num:
    lst[int(i)] += 1
for j in range(len(lst)-1, -1, -1):
    for _ in range(lst[j]):
        print(int(j), end='')
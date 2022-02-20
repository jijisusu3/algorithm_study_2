import sys
sys.stdin = open("5432.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    lst = input()
    sol = cnt = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
        else:
            if lst[i - 1] == '(':
                
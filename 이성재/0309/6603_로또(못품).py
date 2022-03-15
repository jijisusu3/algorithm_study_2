import sys; sys.stdin = open('6603.txt')

a = 1
while a == 1:
    arr = list(int, input().split())
    if arr[0] == 0:
        break
    
    ans = [0] * 6
    if arr[0] == 6:
        for i in arr[1:]:
            print(i, end = ' ')
        print()

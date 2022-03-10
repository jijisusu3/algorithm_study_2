import sys
sys.stdin = open('boj_1759_암호만들기.txt')
input = sys.stdin.readline

L, C = map(int,input().split())
arr = list(input().split())
pick = []

def comb(k, start):
    if k == L:
        print(*pick)

    else:
        for i in range(start, C):
            pick.append(arr[i])
            comb(k + 1, i + 1)
            pick.pop()



comb(0,0)


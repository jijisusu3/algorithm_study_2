import sys
sys.stdin=open('boj_6603_로또.txt')

def comb(k, start):
    if k == R:
        print(*pick)

    else:
        for i in range(start, N):
            pick.append(arr[i])
            comb(k + 1, i + 1)
            pick.pop()

N = 1
while N:
    N, *arr = map(int,input().split())
    R = 6
    pick = []
    comb(0,0)
    if N:
        print()
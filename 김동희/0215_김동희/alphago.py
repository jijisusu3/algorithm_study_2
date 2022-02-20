arr = [[0]*20 for _ in range(20)]

T = int(input())
for t in range(T):
    n, m = map(int,(input().split()))
    arr[n-1][m-1] = 1
print(arr)
        
    
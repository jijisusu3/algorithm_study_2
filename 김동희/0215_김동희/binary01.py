'''
주어지는 10개의 카드

상근이는 8개의 카드

풀이 : 카드의 개수

'''
import sys; sys.stdin=open('binary01.txt')
N = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))
arr1 = sorted(arr1)

for i in range(M):
    cnt = 0
    start = 0
    end = len(arr1)-1
    
    while start <= end:
        mid = (start+end)//2
        
        if arr1[mid] == arr2[i]:
            cnt += 1
            arr1.pop(mid)
            end -= 1
            
        elif arr1[mid] > arr2[i]:
            end = mid -1
            
        else:
            start = mid +1
    print(cnt, end=' ')
        
    
    

    
        
            
        
        
    


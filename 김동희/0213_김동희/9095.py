TC = int(input())

def pattern(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return pattern(n-1) + pattern(n-2) + pattern(n-3)
    
for tc in range(TC):
    n = int(input())
    print(pattern(n))
     
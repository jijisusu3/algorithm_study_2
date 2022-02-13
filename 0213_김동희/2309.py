import sys

lst = []
for i in range(9):
    lst.append(int(sys.stdin.readline()))
    
lst_sum = sum(lst)

for i in range(9):
    for j in range(i+1,9):
        if 100 == lst_sum - (lst[i] + lst[j]): 
            num1,num2=lst[i],lst[j]

            lst.remove(num1)
            lst.remove(num2)
            
            a = [0] * 101
            for i in lst:
                a[i] += 1

            
            for n in range(len(a)):
                count = a[n]
                for m in range(count):
                    print(n)

            break
    if len(lst) != 9:
        break

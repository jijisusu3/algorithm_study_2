a = list(map(int, input().split()))  # input 값을 int로 변환하고 list a 에 저장.
N = len(a)
for j in range(N-1, 0, -1):  # 뒤에서부터 처음까지 -1씩 작아지면서 반복
    for i in range(0, N-1):  # 0부터 N-2 의 위치값까지 비교해야 하기 때문에 N-2+1
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]  # 내림차순으로 변경


for k in a:  # 리스트 값을 k로 도출.
    print(k, end="")  # k를 줄바꿈없이 한 줄로 출력



'''

예시

a= [1,2,3,4]

    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    
    for i in range(len(a)-2):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            
    for i in range(len(a)-3):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

'''
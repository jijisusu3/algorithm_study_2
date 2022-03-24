import sys; sys.stdin = open('1242.txt', 'r')

patterns = {
(3,2,1,1) : 0,
(2,2,2,1) : 1,
(2,1,2,2) : 2,
(1,4,1,1) : 3,
(1,1,3,2) : 4,
(1,2,3,1) : 5,
(1,1,1,4) : 6,
(1,3,1,2) : 7,
(1,2,1,3) : 8,
(3,1,1,2) : 9,
}

hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
          'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]

    # 패턴 비율로 암호 숫자를 찾기
    # 각 행의 맨뒤에서 부터 1찾기 : 1을 찾으면 패턴의 시작을 찾은것!
    is_find = False
    password = []
    for i in range(N):
        idx = M - 1
        # 55번 인덱스 까지만 확인하면 됩니다. , 만약에 55번이 암호코드 시작이 아니면, 암호코드는 올수 없음
        while idx >= 55:
            if data[i][idx] == 1:   #패턴 시작
                is_find = True
                for _ in range(8):
                    c1 = c2 = c3 = c4 = 0   # 패턴의 각 부분의 길이
                    #0101 순서로 오는걸 알고 있으니...
                    # 1의 개수 세서 c4에 저장
                    while data[i][idx] == 1:
                        c4 += 1
                        idx -= 1
                    # 0의 개수 세서 c3에 저장
                    while data[i][idx] == 0:
                        c3 += 1
                        idx -= 1
                    # 1의 개수 세서 c2에 저장
                    while data[i][idx] == 1:
                        c2 += 1
                        idx -= 1
                    # 0의 개수를 세서 c1에 저장
                    c1 = 7 - c2 - c3 - c4
                    idx -= c1
                    #패턴 구했으니! >> 숫자 찾기
                    password.insert(0, patterns[(c1,c2,c3,c4)])
                # print(password)
                break
            else:
                idx -= 1
        if is_find:
            break
    odd_sum = password[0] + password[2] + password[4] + password[6]
    even_sum = password[1] + password[3] + password[5] + password[7]
    result = 0
    if (odd_sum*3 + even_sum)% 10 == 0:
        result = odd_sum + even_sum

    print(f'#{tc}  {result}')
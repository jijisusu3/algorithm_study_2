def solution(name):
    answer = 0
    min_left_right = len(name) - 1  # 왼쪽에서 오른쪽으로만 이동할 때 좌,우 조작 횟수
    next_idx = 0
    for idx, char in enumerate(name):
        # 위, 아래 조작 횟수의 최솟값 구하기
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 좌, 우 조작 횟수의 최솟값 구하기
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1  # 현재 위치 이후 연속된 A 다음의 문자를 가리킴

        # 한 방향으로만 이동하는 경우와, 오른쪽으로 이동했다가 왼쪽으로 이동하는 경우를 비교
        # 예를 들어, "BBBCAAAAAAAAB" 라면 현위치에서 뒤로 돌아가서 뒤 쪽으로 가는거.
        min_left_right = min(min_left_right, idx + idx + len(name) - next_idx)
        # 예를 들어, "BBBBAAAAAAAAAAAAB" 라면 뒤쪽부터 갔다가 다시 돌아서 현 위치까지 오는거.
        min_left_right = min(min_left_right, idx + (len(name) - next_idx) * 2 )

    answer += min_left_right
    return answer

print('출력해보자')
print(solution("JEROEN"))

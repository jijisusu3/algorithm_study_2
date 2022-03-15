def solution(board, moves):
    answer = 0
    N = len(board[0])
    S = []
    for m in moves:
        j = m - 1
        for i in range(N):
            if board[i][j] != 0:
                S.append(board[i][j])
                board[i][j] =0
                break
        if len(S) > 1:
            if S[-2] == S[-1]:
                S.pop()
                S.pop()
                answer += 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
def solution(board, k):
    cnt = 0
    for idx,num_list in enumerate(board):
        for j in range(len(num_list)):
            if idx + j <= k:
                cnt += board[idx][j]
    return cnt
def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    # 지뢰 설치
    mine = []
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                mine.append((i,j))

     # 지뢰가 설치된 곳 주변에 폭탄 설치
    for x, y in mine:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1

    # 안전지대 (폭탄이 설치되지 않은 곳) 카운팅:
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                cnt +=1
    return cnt
def solution(keyinput, board):
    
    start_x = 0
    start_y = 0

    xlim = board[0]//2
    ylim = board[1]//2
    
    for i in keyinput:
        # x좌표
        if i == 'left' and -xlim <= start_x -1:
            start_x -= 1
        elif i == 'right' and start_x + 1 <= xlim:
            start_x += 1
        # y좌표
        elif i == 'down' and -ylim <= start_y -1:
            start_y -= 1
        elif i == 'up' and start_y +1 <= ylim:
            start_y += 1
    return [start_x, start_y]
def solution(dots):
    
    x_coor = [i[0] for i in dots]
    y_coor = [i[1] for i in dots]
    
    return (max(x_coor)-min(x_coor))*(max(y_coor)-min(y_coor))
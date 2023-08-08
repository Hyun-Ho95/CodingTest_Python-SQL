def solution(i, j, k):
    cnt = 0
    ij_list = [ str(x) for x in range(i,j+1)]

    for x_ in ij_list:
        for y_ in x_:
            if str(k) == y_:
                cnt +=1
    return cnt
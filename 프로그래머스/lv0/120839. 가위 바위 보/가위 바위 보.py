def solution(rsp):
    
    winner = []
    
    for idx, i in enumerate(rsp):
        if rsp[idx] =='2':
            winner.append('0')
        elif rsp[idx] =='0':
            winner.append('5')
        else:
            winner.append('2')
            
    return ''.join(winner)
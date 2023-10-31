def solution(myStr):
    for idx,k in enumerate(myStr):
        if (k =='a') or (k =='b') or (k =='c'):
            myStr = myStr.replace(myStr[idx],' ')
    
    answer = myStr.strip().split()
    
    if answer == []:
        return ['EMPTY']
    else:
        return answer
def solution(myString, pat):
    answer = 0
    newSt = ''
    for idx,k in enumerate(myString):
        if k =='A':
            newSt += 'B'
        else:
            newSt += 'A'

    if pat in newSt:
        return 1
    else:
        return 0
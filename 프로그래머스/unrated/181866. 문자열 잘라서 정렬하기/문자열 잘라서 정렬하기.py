def solution(myString):
    myString = myString.split('x')
    answer = []
    for i in myString:
        if i != '':
            answer.append(i)
    return sorted(answer)
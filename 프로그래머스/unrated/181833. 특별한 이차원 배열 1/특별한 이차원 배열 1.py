def solution(n):
    
    answer = []
    for i in range(n):
        array = []
        for j in range(n):
            if i==j:
                array.append(1)
            else:
                array.append(0)
        answer.append(array)
    return answer
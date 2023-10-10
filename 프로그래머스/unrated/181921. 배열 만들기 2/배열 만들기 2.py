def solution(l, r):
    answer = []
    for num in range(l, r+1):
        if set(str(num)) - {'0','5'} == set():
            answer.append(num)
    return answer if answer else [-1]
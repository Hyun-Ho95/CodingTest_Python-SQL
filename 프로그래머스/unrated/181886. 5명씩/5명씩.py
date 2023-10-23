def solution(names):
    answer = []
    for idx, k in enumerate(names):
        if idx % 5 ==0:
            answer.append(k)
    return answer
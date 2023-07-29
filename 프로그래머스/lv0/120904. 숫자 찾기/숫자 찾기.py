def solution(num, k):
    num = list(str(num))
    if str(k) in num:
        answer = (num.index(str(k)))+1
        return answer
    else:
        return -1
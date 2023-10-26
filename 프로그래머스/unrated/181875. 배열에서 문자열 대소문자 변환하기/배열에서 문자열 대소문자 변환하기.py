def solution(strArr):
    for idx,k in enumerate(strArr):
        if idx % 2 ==0:
            strArr[idx] = k.lower()
        else:
            strArr[idx] = k.upper()
    return strArr
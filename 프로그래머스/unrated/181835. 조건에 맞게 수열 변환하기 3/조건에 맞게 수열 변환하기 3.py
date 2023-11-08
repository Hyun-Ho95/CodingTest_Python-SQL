def solution(arr, k):
    result = []
    if k%2==0:
        for i in arr:
            result.append(i+k)
    else:
        for j in arr:
            result.append(j*k)
    return result
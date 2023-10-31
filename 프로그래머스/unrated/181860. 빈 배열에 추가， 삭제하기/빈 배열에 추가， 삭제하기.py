def solution(arr, flag):
    x = []
    for idx,k in enumerate(flag):
        if k == True:
            for _ in range(arr[idx]*2):
                x.append(arr[idx])
        else:
            for _ in range(arr[idx]):
                x.pop()
    return x
def solution(arr):
    res = []
    for idx,k in enumerate(list(map(str,arr))):
        if k == '2':
            res.append(idx)
    return arr[min(res):max(res)+1] if res != [] else [-1]
    
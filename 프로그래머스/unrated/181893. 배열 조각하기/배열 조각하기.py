def solution(arr, query):
    for idx, k in enumerate(query):
        if idx % 2 ==0:
            arr = arr[:k+1]
        else:
            arr = arr[k:]
    return arr
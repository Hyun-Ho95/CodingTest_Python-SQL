def solution(arr, idx):
    result = 0
    for i in range(idx,len(arr)):
        if arr[i] ==1:
            result += i
            return result
    return -1 if result ==0 else result
        

def solution(arr, intervals):
    
    res1 = arr[intervals[0][0]:intervals[0][1]+1]
    res2 = arr[intervals[1][0]:intervals[1][1]+1]
    return res1 + res2
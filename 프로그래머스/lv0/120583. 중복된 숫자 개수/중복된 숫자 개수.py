from collections import Counter

def solution(array, n):
    if n in array:
        return Counter(array).get(n)
    else:
        return 0
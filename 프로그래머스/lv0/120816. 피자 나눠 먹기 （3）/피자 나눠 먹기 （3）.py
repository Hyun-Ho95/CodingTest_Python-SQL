def solution(slices,n):
    if n % slices ==0:
        return n//slices
    else:
        return (n // slices) + 1
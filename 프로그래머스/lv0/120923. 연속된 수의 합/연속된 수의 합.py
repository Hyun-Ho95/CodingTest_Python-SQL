def solution(num, total):
    n = total // num

    if num %2 !=0:
        return list(range( n-(num//2), n+(num//2)+1))
    else:
        return list(range( n-(num//2)+1 ,n+(num//2)+1))
def solution(s):
    s = s.split()
    cnt = 0 
    
    for i in range(len(s)):
        if s[i] != 'Z':
            cnt += int(s[i])
        else:
            cnt -= int(s[i-1])
    return cnt
def solution(myString, pat):
    cnt = 0 
    for i in range(len(myString)):
        while i+len(pat)<=len(myString):
            if myString[i:i+len(pat)]==pat:
                cnt += 1
                break
            else:
                break
    return cnt
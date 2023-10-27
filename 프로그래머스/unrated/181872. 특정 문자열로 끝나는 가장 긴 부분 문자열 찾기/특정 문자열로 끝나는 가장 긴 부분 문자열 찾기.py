def solution(myString, pat):
    if pat in myString:
        idx = myString.rindex(pat)

    if idx + len(pat) >= len(myString):
        return myString
    else:
        return myString[:idx+len(pat)]
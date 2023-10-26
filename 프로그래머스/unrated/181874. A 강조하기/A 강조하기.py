def solution(myString):
    myString = list(myString)  # 문자열을 리스트로 변환
    
    for idx, k in enumerate(myString):
        if k == 'a':
            myString[idx] = 'A'
        elif k != 'A' and k.isupper():
            myString[idx] = k.lower()
    
    myString = ''.join(myString)  # 리스트를 문자열로 변환
    return myString

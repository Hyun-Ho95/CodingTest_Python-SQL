def solution(myString):
    for idx,k in enumerate(myString):
        if k =='a':
            myString = myString.replace(myString[idx],'A')
        elif k != 'A' and k.isupper():
            myString = myString.replace(myString[idx], k.lower())
    return myString
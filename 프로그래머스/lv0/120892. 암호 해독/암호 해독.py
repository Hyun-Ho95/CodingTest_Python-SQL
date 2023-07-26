def solution(cipher, code):
    word = [cipher[i-1] for i in range(1, len(cipher)+1) if i % code == 0 ]
    return ''.join(word)
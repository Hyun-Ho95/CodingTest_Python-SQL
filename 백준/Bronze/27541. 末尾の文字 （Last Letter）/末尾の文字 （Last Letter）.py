# 27541 末尾の文字 (Last Letter) 
N = int(input())
S = input()
if S[N-1] == 'G':
    print(S[:N-1])
else:
    print(S+'G')
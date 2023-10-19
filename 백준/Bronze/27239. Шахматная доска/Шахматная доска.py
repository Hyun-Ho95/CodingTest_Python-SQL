# 27239 Шахматная доска
alphabet = { 1 : 'a'
           , 2 : 'b'
           , 3 : 'c'
           , 4 : 'd'
           , 5 : 'e'
           , 6 : 'f'
           , 7 : 'g'
           , 0 : 'h'}
count = { 0 : '1'
        , 1 : '2'
        , 2 : '3'
        , 3 : '4'
        , 4 : '5'
        , 5 : '6'
        , 6 : '7'
        , 7 : '8'}
n = int(input())
if n % 8==0:
    print(alphabet[n%8] + count[(n//8)-1])
else:
    print(alphabet[n%8] + count[n//8])
# 29725 체스 초보 브실이
chess_dic_b = {'k':0
            ,'p':1
            ,'n':3
            ,'b':3
            ,'r':5
            ,'q':9}
chess_dic_w = {'K':0
            ,'P':1
            ,'N':3
            ,'B':3
            ,'R':5
            ,'Q':9}

white = 0
black = 0
for _ in range(8):
    ware = input()
    for i in ware:
        if i =='.':
            pass
        elif i.isupper():
            white += chess_dic_w[i]
        else:
            black += chess_dic_b[i]
print(white-black)
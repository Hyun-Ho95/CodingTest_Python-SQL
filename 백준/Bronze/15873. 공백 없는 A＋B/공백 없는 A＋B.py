# 15873 공백 없는 A+B
x = input()
if len(x)==4:
    print(20)
elif '10' in x:
    print(int(x.replace('10',''))+10)
else:
    print(int(x[0])+int(x[-1]))
    
# 1076번 저항(Bronze II)
resist = {'black' : ['0',1]
        ,'brown' : ['1',10]
        ,'red' : ['2',100]
        ,'orange' : ['3',1000]
        ,'yellow' : ['4',10000]
        ,'green' : ['5',100000]
        ,'blue' : ['6',1000000]
        ,'violet' : ['7',10000000]
        ,'grey' : ['8',100000000]
        ,'white' : ['9',1000000000]}
ans = ''

col1 = input()
col2 = input()
col3 = input()

ans = ans + resist[col1][0] + resist[col2][0]
print(int(ans)*resist[col3][1])
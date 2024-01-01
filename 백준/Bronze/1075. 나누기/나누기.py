# 1075번 나누기 (Bronze II)
n = input()
f = int(input())
for i in range(100):
    if len(str(i)) < 2:
        n = int(str(n)[:-2] + '0' + str(i))
        if n % f ==0:
            print('0' + str(i))
            break
    else:
        n = int(str(n)[:-2] + str(i))
        if n % f ==0:
            print(str(i))
            break
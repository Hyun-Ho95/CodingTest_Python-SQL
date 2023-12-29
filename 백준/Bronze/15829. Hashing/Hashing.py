# 15829번 Hashing (Bronze II)
l = int(input())
string = input()
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
            'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o': 15, 'p': 16,
            'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24,
            'y': 25, 'z': 26 }
str_num = [ alphabet[i] for i in string ]

cnt = 0
for i in range(l):
        cnt += str_num[i]*(31**i)
print(cnt%1234567891)
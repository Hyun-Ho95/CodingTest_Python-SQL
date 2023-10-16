# 26731 Zaqubiona litera (빠진 알파벳)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char = input()
for i in char:
    if i in alphabet:
        alphabet = alphabet.replace(i,'')
print(alphabet)
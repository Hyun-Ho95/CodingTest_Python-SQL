cro_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cro_alphabet :
    word = word.replace(i, '*') 
print(len(word))
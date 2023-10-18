# 26768 H4x0r
Litera = {'a' : '4'
         ,'e' : '3'
         ,'i' : '1'
         ,'o' : '0'
         ,'s' : '5'}
word = input()
for idx,k in enumerate(word):
    if k in Litera:
        word = word.replace(word[idx],Litera[k])
print(word)
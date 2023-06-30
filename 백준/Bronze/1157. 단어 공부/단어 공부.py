# 1157번 단어공부
word = input().lower() # mississipi
word_uniq = list(set(word)) # m,i,s,p
freq = [] 
for i in word_uniq:
    freq.append(word.count(i)) # [1,4,4,1]
if freq.count(max(freq))>=2:
    print('?')
else:
    print(word_uniq[freq.index(max(freq))].upper())
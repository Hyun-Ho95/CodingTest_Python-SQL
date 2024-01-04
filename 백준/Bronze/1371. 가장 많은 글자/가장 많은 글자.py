# 1371번 가장 많은 글자(BronzeII)
import sys
sentence,alphabet = sys.stdin.read(), [0]*26

for i in sentence:
    if i.islower():
        alphabet[ord(i)-97] += 1
for j in range(len(alphabet)):
    if alphabet[j] == max(alphabet):
        print(chr(j+97),end='')
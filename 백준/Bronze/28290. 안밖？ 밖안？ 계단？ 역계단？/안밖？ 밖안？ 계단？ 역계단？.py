# 28290 안밖? 밖안? 계단? 역계단?
word = input()
if word == 'fdsajkl;' or word == 'jkl;fdsa':
    print('in-out')
elif word == 'asdf;lkj' or word == ';lkjasdf':
    print('out-in')
elif word == 'asdfjkl;':
    print('stairs')
elif word == ';lkjfdsa':
    print('reverse')
else:
    print('molu')
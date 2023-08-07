# 6841 I Speak TXTMSG
short_forms = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later"
}

while True:
    word = input()
    if word == 'TTYL':
        print(short_forms['TTYL'])
        break
    elif word not in short_forms:
        print(word)
    else:
        print(short_forms[word])
    
# 5358 Football Team
while True:
    try:
        name = input()
        new_name = ''
        for i in name:
            if i == 'i':
                new_name += 'e'
            elif i == 'e':
                new_name += 'i'
            elif i == 'I':
                new_name += 'E'
            elif i == 'E':
                new_name += 'I'
            else:
                new_name += i 
        print(new_name)
    except EOFError:
        break
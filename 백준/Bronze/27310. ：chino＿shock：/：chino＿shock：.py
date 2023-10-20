# 27310 :chino_shock:
emoji = input()
level = len(emoji)
for i in emoji:
    if i == ':':
        level += 1
    elif i == '_':
        level += 5
print(level)
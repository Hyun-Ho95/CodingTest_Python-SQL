# 21591 laptop sticker (노트북 스티커)
# wc : 노트북의 너비
# hc : 노트북의 높이
# ws : 노트북 스티커의 너비
# hs : 노트북 스티커의 높이
wc, hc, ws, hs = map(int,input().split())
if wc-ws >=2 and hc-hs >=2:
    print(1)
else:
    print(0)
    
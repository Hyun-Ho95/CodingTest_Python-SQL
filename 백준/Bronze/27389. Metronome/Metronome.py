# 27389 Metronome 
n = int(input())
if len(str(n / 4)) <= 4:
    print(float(str(n/4)+'0'))
else:
    print(n/4)
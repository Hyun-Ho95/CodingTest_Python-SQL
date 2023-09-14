# 18198 Basketball One-on-One
score = input()
score_a = []
score_b = []

cnt = 0
for i in range(int(len(score)/2)):
    if score[cnt]=='A':
        score_a.append(score[cnt:cnt+2])
        cnt += 2
    else:
        score_b.append(score[cnt:cnt+2])
        cnt += 2
        
A = 0
B = 0
for j in score_a:
    A += int(j[-1])
for k in score_b:
    B += int(k[-1])

if max(A,B) == A:
    print('A')
else:
    print('B')
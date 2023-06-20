n = int(input())
score = list(map(int,input().split()))
new_score = []

for i in score:
    mod_i = i/max(score)*100
    new_score.append(mod_i)
print(sum(new_score)/len(new_score))
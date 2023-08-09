# 10039 평균 점수
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

score_list = [a,b,c,d,e]
total_score = 0
for score in score_list:
    if score < 40:
        total_score += 40
    else:
        total_score += score
print(int(total_score/len(score_list)))
        
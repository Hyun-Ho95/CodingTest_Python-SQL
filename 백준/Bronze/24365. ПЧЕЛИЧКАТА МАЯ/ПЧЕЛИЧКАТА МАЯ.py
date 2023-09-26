# 24365 ПЧЕЛИЧКАТА МАЯ(여왕벌 마야)

# 세 수가 동일 == 세 수 모두 세 수의 평균으로 만들어준다 
a,b,c = map(int,input().split())
avg = int((a+b+c)/3)

# cnt : 꿀벌이 움직인 거리(움직인 횟수)
cnt = 0 

# 꿀벌이 c -> b로 이동하는 경우
# c를 평균만큼 만들어주어야 하므로 (c-avg)마리의 꿀벌이 b로 이동하면 c가 avg가 됨
cnt += c-avg # (c-avg)마리의 벌이 1m씩 이동함 -> 1*(c-avg)
b += b + (c-avg) # 기존에 있던 b마리에 (c-avg)마리의 벌 추가

# 꿀벌이 b -> a로 이동하는 경우
# 마찬가지로 b를 평균으로 만들기 위해서 (b-avg)마리의 꿀벌이 이동하면 b가 avg됨
# cnt에 b->a로 이동한 횟수 추가
cnt += b + (c-avg) -avg

# 이 때 8번째 코드에서 cnt에 c-avg가 추가되어 할당 되어있는 상태. 따라서 최종 cnt는
cnt = c-avg + b+ (c-avg) - avg
cnt = 2*c+b -3*(avg)

# 3번째 코드에서 3*(avg) = int(a+b+c)
# 위 식에 대입하면
cnt = 2*c+b -int(a+b+c)
cnt = c-a
print(cnt)
n, m = map(int, input().split())
basket = [ i for i in range(1,n+1) ]
for _ in range(m):
    i, j = map(int, input().split())
    reverse = basket[i-1:j][::-1] # 이 부분이 조금 헷갈렸다 basket에서 슬라이싱&역순 한 값을 변수에 할당
    basket[i-1:j] = reverse # 해당 인덱스의 데이터를 할당한 변수'reverse'값으로 바꿔주기 
print(' '.join(str(n) for n in basket))
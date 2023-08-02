def solution(polynomial):
    
    polynomial_list = polynomial.split()
    num_list = []
    x_list = []
    x_coef_list = []
    
    for i in polynomial_list:
        if i.isdigit():
            num_list.append(int(i))
        elif i != '+':
            x_list.append(i)
    for i in x_list:
        if i=='x':
            x_coef_list.append(1)
        else:
            x_coef_list.append(int(i[:-1]))
    
    a = sum(x_coef_list) # x 계수의 합
    b = sum(num_list) # 상수항의 합
    
    if a ==0: # 일차항의 계수가 0일 때 => 상수항만 출력
        return f'{b}'
    elif a ==1: # 일차항의 계수가 1일 때 
        if b ==0:
            return 'x' # 1x아닌 x로 출력
        else:
            return f'x + {b}' # x + 상수항 
    elif a > 1: # 일차항의 계수가 1보다 클 때
        if b ==0:
            return f'{a}x' # ax 형태로 출력
        else:
            return f'{a}x + {b}' # ax + b 형태로 출력
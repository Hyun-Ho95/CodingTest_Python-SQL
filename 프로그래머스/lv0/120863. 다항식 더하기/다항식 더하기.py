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
            
    if sum(x_coef_list) ==0:
        return f'{sum(num_list)}'
    elif sum(x_coef_list) ==1:
        if sum(num_list) ==0:
            return 'x'
        else:
            return f'x + {sum(num_list)}'
    elif sum(num_list) == 0:
        return f'{sum(x_coef_list)}x'
    elif sum(x_coef_list) > 1:
        if sum(num_list) ==0:
            return f'{sum(x_coef_list)}x'
        else:
            return f'{sum(x_coef_list)}x + {sum(num_list)}'
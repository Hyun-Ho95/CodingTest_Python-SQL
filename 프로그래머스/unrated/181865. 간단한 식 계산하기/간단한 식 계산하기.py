def solution(binomial):
    binomial = binomial.split(' ')
    if binomial[1] == '+':
        return int(binomial[0]) + int(binomial[-1])
    elif binomial[1] == '-':
        return int(binomial[0]) - int(binomial[-1])
    else:
        return int(binomial[0]) * int(binomial[-1])
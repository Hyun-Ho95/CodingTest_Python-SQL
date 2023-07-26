def solution(numbers):
    
    num_list = {"zero":0, "one":1, "two":2,
                "three":3, "four":4, "five":5, "six":6, 
                "seven":7, "eight":8 , "nine":9 }
    
    for num in num_list:
        if num in numbers:
            numbers = numbers.replace(num, str(num_list[num]))
    return int(numbers)
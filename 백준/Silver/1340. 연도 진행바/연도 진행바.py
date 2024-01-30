# 1340번 연도 진행바(Silver V)
month, day, year, time = input().split()
day = int(day[:-1])
year = int(year)
hour, minute = map(int,time.split(':'))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_days =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# days(일)
total_days = 0

if year%400==0 or (year%4==0 and year%100!=0):
    month_days[1] += 1

total_days += sum(month_days[:months.index(month)]) + day - 1

# time(시,분)
total_time = (total_days*24*60) + (hour*60) + minute
divide_time = sum(month_days)*24*60
percent = (total_time / divide_time)*100
print(percent)
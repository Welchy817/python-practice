# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

month, day, year = list(map(int, input().split()))
weekdays = list(calendar.day_name)
cal = calendar.Calendar(firstweekday=0)
target = cal.monthdays2calendar(year, month)
for days in target:
    for date in days:
        if date[0] == day:
            print(weekdays[date[1]].upper())
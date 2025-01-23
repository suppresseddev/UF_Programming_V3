# Write a program named Lab1_C.py that will calculate the number of days between 2 dates.
#
# Input:
# Enter the year for date 1:
# Enter the month for date 1:
# Enter the day for date 1:
# Enter the year for date 2:
# Enter the month for date 2:
# Enter the day for date 2:
#
# Output:
# The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {difference} days!
#
# You may assume:
# All inputs are valid integers greater than 0
# Years always have exactly 12 months
# Months always have exactly 30 days
#
# Examples:
#
# Enter the year for date 1: 2004
# Enter the month for date 1: 1
# Enter the day for date 1: 16
# Enter the year for date 2: 2024
# Enter the month for date 2: 5
# Enter the day for date 2: 17
# The difference between 1/16/2004 and 5/17/2024 is 7321 days!
#
#
# Enter the year for date 1: 1999
# Enter the month for date 1: 12
# Enter the day for date 1: 30
# Enter the year for date 2: 2000
# Enter the month for date 2: 1
# Enter the day for date 2: 1
# The difference between 12/30/1999 and 1/1/2000 is 1 days!

#Date 1 : 1/12/2005
#Date 2 : 12/15/2003
from datetime import *
debug = True
def diffInDays(year1, month1, day1, year2, month2, day2):
    print(f"Enter the year for date 1: {year1}")
    print(f"Enter the month for date 1: {month1}")
    print(f"Enter the day for date 1: {day1}")
    print(f"Enter the year for date 2: {year2}")
    print(f"Enter the month for date 2: {month2}")
    print(f"Enter the day for date 2: {day2}")
    date1 = (date(year1, month1, day1))
    date2 = (date(year2, month2, day2))
    if date1 > date2:
        timebetween = int((date1 - date2).days)
        correction1 = round((date1.year - date2.year)*5.25)
        correction2 = (int(date1.year) // 4) - (int(date2.year) // 4)
    else:
        timebetween = int((date2 - date1).days)
        correction1 = round((date2.year - date1.year) * 5.25)
        correction2 = (int(date2.year) // 4) - (int(date1.year) // 4)
    if debug:
        print(f"timebetween: {timebetween}")
        print(f"Correction1: {correction1}")
        print(f"Correction2: {correction2}")
    print(f"The difference betweeen {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {timebetween-correction1-correction2} day(s)!")

#diffInDays(2005,1,12,2003,12,15)

diffInDays(1999,12,30,2000,1,1)

diffInDays(2004, 1, 16,2024,5,17)
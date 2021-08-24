# Input the date
date = input("Enter the Date in dd/mm/yyyy format")
d = int(date[:2])
m = int(date[3:5])
y = int(date[6:])


# Returns if the present year is a leap year or not
def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


# Returns the number of days upto the previous year
def no_of_leap_year(y):
    return (y-1)//4-(y-1)//100+(y-1)//400 if y > 1 else 0


# Returns the total number of days unto the previous year
def days_upto_previous_year(y):
    return no_of_leap_year(y)*366+(y-1-no_of_leap_year(y))*365 if y > 1 else 0


# Returns the days unto the previous month in that year
def days_previous_month(m, y):
    if m > 2:
        if m <= 8:
            return (m // 2) * 31 + (m // 2 - 1) * 30 - 1 if leap_year(y) == 1 else (m // 2) * 31 + (m // 2 - 1) * 30 - 2
        else:
            return ((m + 1) // 2) * 31 + ((m - 2) // 2) * 30 - 1 if leap_year(y) == 1 else ((m + 1) // 2)*31 + ((m - 2) // 2) * 30 - 2
    return (m//2)*31


# According to Gregorian Calender
def day(d):
    if d % 7 == 0:
        return 'Sunday'
    elif d % 7 == 1:
        return 'Monday'
    elif d % 7 == 2:
        return 'Tuesday'
    elif d % 7 == 3:
        return 'Wednesday'
    elif d % 7 == 4:
        return 'Thursday'
    elif d % 7 == 5:
        return 'Friday'
    else:
        return 'Saturday'


# Calculates the total number of days since 01/01/0001
days = days_upto_previous_year(y)+days_previous_month(m, y)+d
print(days)
print(day(days))
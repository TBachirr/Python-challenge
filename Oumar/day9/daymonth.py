year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def day_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapyear(year):
        month_days[1] = 29
    return month_days[month - 1]    

print(day_in_month(year, month))

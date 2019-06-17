# Function gives you the correct day of the year for any day of any year up to the year 3000. It accounts for leap years as well.

def isYearLeap(year):
    
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
def daysInMonth(year, month):
    months_lenghts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month > 12:
        print("There are only 12 months in a year")
        return None
        
    if year > 3000:
        print("The year can't be higher than 3000")
        return None
    
    if isYearLeap(year) == True and month == 2:
        return months_lenghts[month - 1] + 1
    else:
        return months_lenghts[month -1]
        
        
def dayOfYear(year, month, day):
    sumofdays = day
    #months_lenghts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #if isYearLeap(year) == True:
        #months_lenghts[1] = daysInMonth(year, 2)
    
    if year < 1512 or month > 12 or day > 31:
        return None
    
    for i in range(1,month):
        sumofdays += daysInMonth(year, i)
        #sumofdays += months_lenghts[i]
    
    print('The day of the year is the', end=" ")
    return sumofdays
    
print(dayOfYear(2001, 3, 1))
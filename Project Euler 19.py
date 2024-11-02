# 1900 is NOT a leap year
# 2000 IS a leap year

yearList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYearList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



# monday = 0, tuesday = 1 ... sunday = 6

def currentDay(startDay, daysPassed):
    return ((daysPassed % 7 + startDay) % 7) 

dayOfWeek = currentDay(0, 365)
sundays = 0

for year in range(1901, 2001):

    if year % 4 == 0:
        for month in leapYearList:
            dayOfWeek = currentDay(dayOfWeek, month)
            if dayOfWeek == 6:
                sundays += 1
    
    else:
        for month in yearList:
            dayOfWeek = currentDay(dayOfWeek, month)
            if dayOfWeek == 6:
                sundays += 1 
    

print(sundays)

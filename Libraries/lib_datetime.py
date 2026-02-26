import datetime

now = datetime.datetime.now() #Get now

#Format of datetime is YYYY-MM-DD HH:MM:SS.ms

#Creation of dates
whenICreatedThisFile = datetime.datetime(year=2026, month=2, day=26, hour=19, minute=18, second=14, microsecond=20059) #sorry the microsecond isn't accurate
dayICreatedThisFile = datetime.datetime(2026, 2, 26)

#Formatting to readable strings
datetime.datetime.strftime()

dayICreatedThisFile.strftime("%a") #Weekday, short
dayICreatedThisFile.strftime("%A") #Weekday, long
dayICreatedThisFile.strftime("%w") #Weekday, number (0-6)
dayICreatedThisFile.strftime("%d") #Day of month, (0-31)
dayICreatedThisFile.strftime("%b") #Month name, short
dayICreatedThisFile.strftime("%B") #Month name, long
dayICreatedThisFile.strftime("%m") #Month number, (0-12)
dayICreatedThisFile.strftime("%y") #Year, short (no century, e.g. 2018 -> 18)
dayICreatedThisFile.strftime("%Y") #Year

dayICreatedThisFile.strftime("%H") #Hour Millitary
dayICreatedThisFile.strftime("%I") #Hour 0-12
dayICreatedThisFile.strftime("%p") #AM/PM
dayICreatedThisFile.strftime("%M") #Minute
dayICreatedThisFile.strftime("%S") #Second
dayICreatedThisFile.strftime("%f") #Micro second

#To go forward / backward
dayAfter = dayICreatedThisFile+datetime.timedelta(days=1) #change the value inside the brackets to change increment. Can add and subtract.
dayBefore = dayICreatedThisFile-datetime.timedelta(days=1)

#Not datetime but useful to integrate with it
import calendar

year, month = 2026, 2
calendar.monthrange(year, month) #Returns (start_date, num_days)
#so
month_dur_days = calendar.monthrange(year, month)[1]
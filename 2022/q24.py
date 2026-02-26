#The daily grind

import sys, datetime, calendar

#Functions

def forty_hour(start_date, final_date):
    current_date = start_date
    total_days = 0
    
    while current_date != final_date+datetime.timedelta(days=1):
        if (int(current_date.strftime("%w")) >= 1) and (int(current_date.strftime("%w")) <= 5):
            total_days += 1
        
        current_date = current_date+datetime.timedelta(days=1)

    total_hours = total_days * 8
    return (total_days, total_hours)

def four_ten(start_date, final_date):
    current_date = start_date
    total_days = 0
    
    while current_date != final_date+datetime.timedelta(days=1):
        if (int(current_date.strftime("%w")) >= 1) and (int(current_date.strftime("%w")) <= 4):
            total_days += 1
        
        current_date = current_date+datetime.timedelta(days=1)

    total_hours = total_days * 10
    return (total_days, total_hours)

def figure_out_fridays(year, isFirst):
    current_date = datetime.datetime(year, 1, 1)
    list_friday = []
    is_current_friday = isFirst
    while current_date != datetime.datetime(year+1, 1, 1):
        if (int(current_date.strftime("%w")) == 5):
            if(is_current_friday):
                list_friday.append(current_date)
                is_current_friday = False
            else:
                is_current_friday = True
        
        current_date = current_date+datetime.timedelta(days=1)

    return list_friday

def workweek9_80A(start_date, final_date, year):
    friday_list = figure_out_fridays(year, True)

    current_date = start_date
    total_days = 0
    total_hours = 0
    while current_date != final_date+datetime.timedelta(days=1):
        if (int(current_date.strftime("%w")) >= 1) and (int(current_date.strftime("%w")) <= 4):
            total_days += 1
            total_hours += 9
        if(current_date in friday_list):
            total_days += 1
            total_hours += 8
        
        current_date = current_date+datetime.timedelta(days=1)

    return (total_days, total_hours)

def workweek9_80B(start_date, final_date, year):
    friday_list = figure_out_fridays(year, False)

    current_date = start_date
    total_days = 0
    total_hours = 0
    while current_date != final_date+datetime.timedelta(days=1):
        if (int(current_date.strftime("%w")) >= 1) and (int(current_date.strftime("%w")) <= 4):
            total_days += 1
            total_hours += 9
        if(current_date in friday_list):
            total_days += 1
            total_hours += 8
        
        current_date = current_date+datetime.timedelta(days=1)

    return (total_days, total_hours)

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    day, month, year = map(int, sys.stdin.readline().rstrip().split("/"))

    date = datetime.datetime(year, month, day)

    month_duration = calendar.monthrange(year, month)[1]

    #Get Last Friday
    temp_day = 1
    monday_found = False
    last_friday = -1
    last_friday_datetime = None
    first_monday = -1
    while temp_day < (month_duration + 1):
        temp_date = datetime.datetime(year, month, temp_day)
        if(temp_date.strftime("%A")) == "Friday":
            last_friday = temp_day
            last_friday_datetime = datetime.datetime(year, month, last_friday)
        temp_day += 1
    
    #Get Monday at the start of that period
    temp_monday = 1
    temp_date = datetime.datetime(year, month, temp_monday)
    
    if temp_date.strftime("%A") != "Monday":
        #If sunday/saturday set to next monday
        if int(temp_date.strftime("%w")) == 0:
            temp_date = temp_date+datetime.timedelta(days=1)
        if int(temp_date.strftime("%w")) == 6:
            temp_date = temp_date+datetime.timedelta(days=2)
        

        #If weekday (not monday), set it to that monday
        if (int(temp_date.strftime("%w")) >= 2) and (int(temp_date.strftime("%w")) <= 5):
            steps = int(temp_date.strftime("%w")) - 1
            temp_date = temp_date-datetime.timedelta(days=steps)

    first_monday = temp_date

    #Different work weeks
    forty_hour_days = forty_hour(first_monday, last_friday_datetime)[0]
    four_ten_days = four_ten(first_monday, last_friday_datetime)[0]
    nine_eighty_A_days = workweek9_80A(first_monday, last_friday_datetime, year)[0]
    nine_eighty_B_days = workweek9_80B(first_monday, last_friday_datetime, year)[0]

    print(f"{forty_hour_days} {four_ten_days} {nine_eighty_A_days} {nine_eighty_B_days}")
    
#!/usr/bin/env python3

import sys
import random
import calendar
from datetime import date, timedelta

#Generates a random date for a given month and year
def random_date(year, month):
    start_date = date(year, month, 1)
    
    #Small bug in function produced by chatGPT, the below line is what it
    #originally produced. This works for all but December as date() expects the
    #month entry to be in range [1,12]
    # end_date   = date(year, month+1, 1) - timedelta(days=1)
    
    if (month < 12):
        end_date   = date(year, month + 1, 1) - timedelta(days=1)
    else:
        end_date   = date(year + 1, 1, 1) - timedelta(days=1)

    random_day = random.randint(start_date.day, end_date.day)
    return date(year, month, random_day)

#Generates 4-6 random dates per month of a given year
def print_random_dates_per_month(year):
    for month in range(1, 13):
        print(calendar.month_name[month])

        #Generate the dates
        dates = []
        num_dates = random.randint(4, 6)
        while len(dates) < num_dates:
            random_dt = random_date(year, month)
            if random_dt not in dates:
                dates.append(random_dt)
        
        #Sort then print the dates that were generated
        dates.sort()
        for dt in dates:
            print("%02d/%02d/%d" %(dt.month, dt.day, dt.year))
        print()

    return

#Acquire year
if (len(sys.argv) > 1):
    year = int(sys.argv[1])
else:
    year = date.today().year

print_random_dates_per_month(year)
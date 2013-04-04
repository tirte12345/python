from dateutil import rrule
from datetime import datetime

sum = 0
for month in range(1,13):
    workdays = [0, 1, 2, 3, 4]
    days = rrule.rrule(rrule.DAILY, dtstart=datetime(2013,month,1),
    until=datetime(2013,3,31), byweekday=workdays)
    sum = sum + days.count()
    
print (sum)

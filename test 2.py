from datetime import date
import datetime
import calendar

month = datetime.datetime.now().month
end_date = calendar.monthrange(2013,month) [1]

def workdaycount(first, second, inc = 0):
   if first == second:
      return 0
   import math
   if first > second:
      first, second = second, first
   if inc:
      from datetime import timedelta
      second += timedelta(days=1)
   interval = (second - first).days
   weekspan = int(math.ceil(interval / 7.0))
   if interval % 7 == 0:
      return interval - weekspan * 2
   else:
      wdf = first.weekday()
      if (wdf < 6) and ((interval + wdf) // 7 == weekspan):
         modifier = 0
      elif (wdf == 6) or ((interval + wdf + 1) // 7 == weekspan):
         modifier = 1
      else:
         modifier = 2
      return interval - (2 * weekspan - modifier)

print (workdaycount(date(2013, month, 1), date(2013,month, end_date), 1))

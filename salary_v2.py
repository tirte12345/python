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

workday_count = (workdaycount(date(2013, month, 1), date(2013,month, end_date), 1))


print("Where does my salary go?")

while True:
    try:
        x = input("Your gross salary: ")
        y = input("Your total dependant: ")
        z = input("Your total unpaid leave for that month: ")
      
        contracted_salary = int(x)
        total_dependant = int(y)
        unpaid_leave = int(z)
           
        
        actual_workday = workday_count - unpaid_leave
        gross_salary = contracted_salary / workday_count * actual_workday
        
        if contracted_salary >= 21000000:
            salary_for_SIHIUI = 21000000
        else: salary_for_SIHIUI = contracted_salary

        SI = salary_for_SIHIUI*0.07
        HI = salary_for_SIHIUI*0.015
        UI = salary_for_SIHIUI*0.01

        total_insurance = SI+HI+UI

        personal_deduction = int(4000000)
        dependant_deduction = total_dependant*1600000

        total_deduction = personal_deduction + dependant_deduction + total_insurance

        if gross_salary - total_deduction > 0:
            assessible = gross_salary - total_deduction
        else: assessible = 0

        if assessible <= 5000000:
            pit = assessible*0.05
        else:
            if assessible <= 10000000:
                pit = assessible*0.1-250000
            else:
                if assessible <= 18000000:
                    pit = assessible*0.15-750000
                else:
                    if assessible <= 32000000:
                        pit = assessible*0.2-1650000
                    else:
                        if assessible <= 52000000:
                            pit = assessible*0.25-3250000
                        else:
                            if assessible <= 80000000:
                                pit = assessible*0.3-5850000
                            else: pit = assessible*0.35-9850000
                            
        net_salary = gross_salary - pit - total_insurance
       
        print("Your net salary is: " + str(net_salary))
        print("Your total insurance payment is: " + str(total_insurance))
        print("Your personal income tax is: " + str(pit))

    except ValueError:
        print("Please fully input all variables in number")
    
    yes_no_input = input("Do you want to continue? (y/n): ")

    if yes_no_input != "y":
        break
        
print("Thank you and goodbye")



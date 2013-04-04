print("Where does my salary go?")

while True:
    try:
        x = input("Your gross salary: ")
        y = input("Your total dependant: ")

        gross_salary = int(x)
        total_dependant = int(y)

        if gross_salary >= 21000000:
            salary_for_SIHIUI = 21000000
        else: salary_for_SIHIUI = gross_salary

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



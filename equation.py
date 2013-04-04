import math
print("Welcome to Quadratic Equation Solver")

while True:

    print("Please input your variables: a, b, c")
    try:
        a_input = input("a: ")
        b_input = input("b: ")
        c_input = input("c: ")

        a = int(a_input)
        b = int(b_input)
        c = int(c_input)

        delta = b*b - 4*a*c
        if a == 0 and b == 0 and c == 0:
            print("There are indefinite solutions for the equation")
        else:
            if a == 0 and b == 0:
                print("There is no roots")
            else:

                if a == 0 and b != 0:
                    x = -c/b
                    print(("x = ") + str(x))

                else:

                    if delta < 0:
                        print("There is no solutions")
                    else:
                        if delta > 0:
                            delta_squareroot = math.sqrt(delta)
                            x1 = (-b+delta_squareroot)/(2*a)
                            x2 = (-b-delta_squareroot)/(2*a)
                            print(("delta squareroot = ") + str(delta_squareroot))
                            print(("X1 = ") + str(x1))
                            print(("X2 = ") + str(x2))
                        else:
                            delta == 0
                            x1 = -(b/(2*a))
                            x2 = -(b/(2*a))
                            print(("X1 = ") + str(x1))
                            print(("X2 = ") + str(x2))

    except ValueError:
        print("Please fully input all variables in number")
    yes_no_input = input("Do you want to continue? (y/n): ")

    if yes_no_input != "y":
        break



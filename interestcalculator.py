def compound_interest(principal_amount, rate, time):
    amount = principal_amount * (pow((1 + rate/100), time))
    CI = amount - principal_amount
    print("The compound interest is: ", str(CI))

def simple_interest(principal_amount, rate, time):
    amount = (principal_amount * rate * time)/100
    print("The simple interest is: ", str(amount))

start_program = str(input("Type yes to start program: "))
while start_program == "yes":
    type_of_program = str(input("Type simple or compound: "))
    if type_of_program == "compound":
        principal_amount = float(input("Enter your principal amount: "))
        rate = float(input("Enter your rate: "))
        time = float(input("Enter your time: "))
        compound_interest(principal_amount, rate, time)
        start_program = str(input("If you want to restart program, type yes, or no to end it: "))

    if type_of_program == "simple":
        principal_amount = float(input("Enter your principal amount: "))
        rate = float(input("Enter your rate: "))
        time = float(input("Enter your time: "))
        simple_interest(principal_amount, rate, time)
        start_program = str(input("If you want to restart program, type yes, or no to end it: "))

    if start_program == "no":
        break
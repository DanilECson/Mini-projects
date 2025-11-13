def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/b

start_program = str(input("Type yes to start the program: "))
while start_program == "yes":
    a = float(input("Type the first number: "))
    type_of_operation = str(input("Type 'add/+', 'subtract/-', 'multiply/*', 'divide//': "))
    b = float(input("Type the second number: "))
    if type_of_operation == "add" or type_of_operation == "+":
        result = add(a, b)
        print("Your answer is ", str(result))
        start_program = str(input("If you wish to continue, type 'yes' or 'no' to stop the program: "))
    if type_of_operation == "subtract" or type_of_operation == "-":
        result = subtract(a, b)
        print("Your answer is ", str(result))
        start_program = str(input("If you wish to continue, type 'yes' or 'no' to stop the program: "))
    if type_of_operation == "multiply" or type_of_operation == "*":
        result = multiply(a, b)
        print("Your answer is ", str(result))
        start_program = str(input("If you wish to continue, type 'yes' or 'no' to stop the program: "))
    if type_of_operation == "divide" or type_of_operation == "/":
        result = divide(a, b)
        print("Your answer is ", str(result))
        start_program = str(input("If you wish to continue, type 'yes' or 'no' to stop the program: "))

    if start_program == "no":
        print("Thank you for using my calculator :)")
        break


first_number = float(input("please enter the first number: "))
second_number = float(input("please enter the second number: "))
operation = input("please enter the math operation: ")

addition = first_number +  second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
percentage = first_number % second_number

while operation == "+":
    print(first_number, operation , second_number , "=  " , addition)
elif operation == "-":
    print(first_number, operation , second_number , "=  " , subtraction )
elif operation == "*":
    print(first_number, operation , second_number , "=  " , multiplication)
elif operation == "/":
    print(first_number,operation,second_number, "=  " , division )
elif operation == "%":
    print(first_number,operation,second_number, "=  ", percentage)
else:
    print("****** Unknown Command ******")


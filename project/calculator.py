# python basic calculator 

operator = input("Enter a operator(+,-,*,/): ")
num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a Second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print(f"{operator} is not valid operator!!")
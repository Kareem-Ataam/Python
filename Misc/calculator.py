"""
Simple calculator using python
Input:
    -- First number
    -- Operator
    -- Second number
Output:
    -- Printing the result of the mathematical operation
"""
# Validating the first number
while True:
    try:
        num1 = float(input("Enter the first number: "))
        break
    except:
        print("Only numbers are allowed")
        ValueError
# Validating the operator
while True:
    operator = input("Enter the operator (+, -, /, *): ")
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        break
    print("Enter valid operator")
# Validating the second number
while True:
    try:
        num2 = float(input("Enter the second number: "))
        break
    except:
        print("Only numbers are allowed")
        ValueError

# Performing the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
else:
    result = num1 / num2

# Rounding and outputting the result
result = round(result,2)
print("===============================")
print(str(num1) + " " + operator + " " + str(num2) + " = " + str(result))
print("===============================")
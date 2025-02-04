def calculator():
    operation = input("Enter the operation: ")
    num1 = float(input("Enter the first operand: "))
    num2 = float(input("Enter the second operand: "))
    ans = 0.0
    if operation == 'add':
        ans = num1 + num2
    if operation == 'sub':
        ans = num1 - num2
    if operation == 'mul':
        ans = num1 * num2
    if operation == 'div':
        ans = num1 / num2
    print(f"Result is {round(ans, 2)}")
calculator()
#Scientific Calculator!
#This should be fun because it's my style of program.
import math

#Global Variables
#Total of all calculations:
sum_calc = 0.0
#Total calculations completed:
calcs = 0
#Last result:
last_result = 0.0

#Input Functions:
#Menu Navigation
validmenu = [0, 1, 2, 3, 4, 5, 6, 7]
menu = ("""Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average
""")
def menuInput():
    userInput = int(input('Enter Menu Selection: '))
    if userInput in validmenu:
        return userInput
    else:
        print('Error: Invalid selection!')
        return 'ERROR'
#Operand Input
def oInput(case):
    global last_result
    userInput = input(f'Enter {str(case).lower()} operand: ')
    if str(userInput).upper() == "RESULT":
        userInput = last_result
        return userInput
    else:
        try:
            userInput = float(userInput)
            return userInput
        except ValueError:
            print('Error: invalid input!')
            return 'ERROR'
#Math Functions
#Addition
def addition():
    global last_result
    global calcs
    input1 = oInput('first')
    if input1 == 'ERROR':
        return()
    input2 = oInput('second')
    if input2 == 'ERROR':
        return()
    last_result = input1 + input2
    calcs += 1
    global sum_calc
    sum_calc += last_result
#Subtraction
def subtraction():
    global last_result
    global calcs
    input1 = oInput('first')
    if input1 == 'ERROR':
        return()
    input2 = oInput('second')
    if input2 == 'ERROR':
        return()
    last_result = input1 - input2
    calcs += 1
    global sum_calc
    sum_calc += last_result
#Multiplication
def multiplication():
    global last_result
    global calcs
    input1 = oInput('first')
    if input1 == 'ERROR':
        return()
    input2 = oInput('second')
    if input2 == 'ERROR':
        return()
    last_result = input1 * input2
    calcs += 1
    global sum_calc
    sum_calc += last_result
#Division
#limit, no 0 as 2nd operand
def division():
    global last_result
    global calcs
    input1 = oInput('first')
    if input1 == 'ERROR':
        return()
    input2 = oInput('second')
    if input2 == 'ERROR':
        return()
    if input2 == 0.0:
        print('Error: invalid input!')
        return()
    last_result = input1 / input2
    calcs += 1
    global sum_calc
    sum_calc += last_result
#Exponentiation
def exponentiation():
    global last_result
    global calcs
    input1 = oInput('first')
    if input1 == 'ERROR':
        return()
    input2 = oInput('second')
    if input2 == 'ERROR':
        return()
    last_result = input1 ** input2
    calcs += 1
    global sum_calc
    sum_calc += last_result
#Logarithim
#limit, nothing below 0 and cannot be equal to 1 for 1st operand
#limit, nothing 0 or below for 2nd operand
def logarithim():
    global last_result
    global calcs
    input1 = oInput('first')
    if input1 == 'ERROR':
        return()
    if input1 < 0.0:
        print('Error: invalid input!')
        return()
    if input1 == 1.0:
        print('Error: invalid input!')
        return()
    input2 = oInput('second')
    if input2 == 'ERROR':
        return()
    if input2 <= 0.0:
        print('Error: invalid input!')
        return()
    last_result = math.log(input2, input1)
    calcs += 1
    global sum_calc
    sum_calc += last_result

#Display Average
#limit, canot display if total calculations less than 1
def average():
    global sum_calc
    global calcs
    print(f"Sum of calculations: {sum_calc}")
    print(f"Number of calculations: {calcs}")
    print(f"Average of calculations: {(sum_calc / calcs):.2f}")
#The Loop
while True:
    print(f"Current Result: {last_result}\n")
    print(menu)
    while True:
        nav = menuInput()
        if nav == 'ERROR':
            continue
        if nav == 0:
            print("Thanks for using this calculator. Goodbye!")
            exit()
        if nav == 1:
            addition()
            break
        if nav == 2:
            subtraction()
            break
        if nav == 3:
            multiplication()
            break
        if nav == 4:
            division()
            break
        if nav == 5:
            exponentiation()
            break
        if nav == 6:
            logarithim()
            break
        if nav == 7:
            if calcs < 1:
                print('Error: No calculations yet to average!')
                continue
            else:
                average()
                continue

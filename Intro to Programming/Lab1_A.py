# Program A
#
# Write a program named Lab1_A.py that will convert a temperature from Celsius to Fahrenheit.
#
# All outputs should be rounded to one decimal place.
#
# Input:
# Enter the temperature in Celsius:
#
# Output:
# That is {temperature} degrees Fahrenheit!
#
# You may assume:
# All inputs are valid numbers
#
# Examples:
#
# Enter the temperature in Celsius: 0
# That is 32.0 degrees Fahrenheit!

def tempToF(temp_c):
    print(f"Enter the temperature in Celsius: {temp_c}")
    temp_f = temp_c * 9/5 + 32
    temp_f = round(temp_f, 1)
    print(f"That is {temp_f} degrees Fahrenheit!")
    print()
tempToF(-20)
tempToF(40.4)

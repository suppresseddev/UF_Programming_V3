# Program B
#
# Write a program named Lab1_B.py that will calculate the sales tax on a purchased item.
#
# All outputs should be rounded to two decimal places.
#
# Input:
# Enter the price of the item:
# Enter the sales tax percentage:
#
# Output:
# Your total is ${price}
#
# You may assume:
# All inputs are valid numbers greater than or equal to 0
# Sales tax is entered as a percentage
#
# Examples:
#
# Enter the price of the item: 100
# Enter the sales tax percentage: 7
# Your total is $107.00
#
# Enter the price of the item: 15.73
# Enter the sales tax percentage: 11
# Your total is $17.46
#
# Enter the price of the item: 1289.23
# Enter the sales tax percentage: 3.4
# Your total is $1333.06

def addTax():
    price = float(input(f"Enter the price of the item: "))
    taxrate = float(input(f"Enter the sales tax percentage: "))
    total = float(price) * (1.00+(float(taxrate)/100.00))
    total = round(total, 2)
    print(f"Your total is ${total:.2f}")

addTax()

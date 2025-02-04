# Discounts
# Write a program called discounts.py that will calculate the final price of an item after applying several discounts. The discounts will apply multiplicatively to each other. The user will enter:
# Price of the item
# Is it black friday
# Do you have a coupon
# Do you have an employee discount
# The available discounts are:
# black friday (40% off), coupon (5% off), employee discount (20% off)

def discounter():
    price = float(input("Enter the price: "))
    blackfriday = str(input("Is it black friday [y/n]: ")).upper()
    coupon = str(input("Do you have a coupon [y/n]: ")).upper()
    discount = str(input("Do you have an employee discount [y/n]: ")).upper()
    if blackfriday == "Y":
        price = price - (price*.4)
    if coupon == "Y":
        price = price - (price*.05)
    if discount == "Y":
        price = price - (price*.2)
    print(f"The final price is: ${price:.2f}")
discounter()
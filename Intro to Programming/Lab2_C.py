#Improved temperature converter!
def tempTo():
    #Ask for base unit. (Always convert to celsius first)
    o_unit = str(input("Enter the unit you are converting from: ")).upper()
    d_unit = str(input("Enter the unit you are converting to: ")).upper()
    #Normalize in C
    temp_inC = 0.00
    if o_unit == "FAHRENHEIT":
        otemp = float(input("Enter the temperature in Fahrenheit: "))
        temp_inC = (otemp-32)*5/9
    if o_unit == "CELSIUS":
        otemp = float(input("Enter the temperature in Celsius: "))
        temp_inC = otemp
    if o_unit == "KELVIN":
        otemp = float(input("Enter the temperature in Kelvin: "))
        temp_inC = otemp - 273.15
    #Convert to desired:
    dtemp = 0.00
    if d_unit == "FAHRENHEIT":
        dtemp = (temp_inC*(9/5))+32
    if d_unit == "CELSIUS":
        dtemp = temp_inC
    if d_unit == "KELVIN":
        dtemp = temp_inC + 273.15
    print(f"That is {dtemp:.1f} degrees {d_unit.capitalize()}.")
tempTo()
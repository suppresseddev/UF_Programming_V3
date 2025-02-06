#This one may be a doozy:
def taxrate(salary):
    caps = [11600, 47150, 100525, 191950, 243725, 609350]
    taxable = [11600, (47150 - 11600), (100525 - 47150), (191950 - 100525), (243725 - 191950), (609350 - 243725)]
    taxrates = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35]
    total_owed = 0.00
    income = salary
    for i, cap in enumerate(caps):
        if income > cap:
            income -= taxable[i]
            total_owed += taxrates[i]*(taxable[i])
        else:
            total_owed += taxrates[i]*income
            income = 0
            break
    if income > 0:
        total_owed += income*0.37
    return(total_owed)

def turboTax():
    income = float(input('Enter your total income this year: '))
    # income = 10.50
    owed = taxrate(income)
    print(f"You owe ${owed:.2f} this year.")
turboTax()

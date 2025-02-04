# Write a program called animals.py that guesses what animal something is based on a couple questions.
# If it has legs and is fluffy, it’s a cat!
# If it has legs and is not fluffy, it’s a gator!
# If it does not have legs and lives on land, it’s a snake!
# If it does not have legs and does not live on land, it’s a shark!
def classifier():
    #Ask for legs?
    legs = str(input("Does it have legs [y/n]: ")).upper()
    #Only if legs
    if legs == 'Y':
        fluffy = str(input("Is it fluffy [y/n]: ")).upper()
        if fluffy == 'Y':
            print("It's a cat!")
        else:
            print("It's a gator!")
    #If NOT legs
    if legs == 'N':
        landlubber = str(input("Does it live on land [y/n]: ")).upper()
        if landlubber == 'Y':
            print("It's a snake!")
        else:
            print("It's a shark!")
classifier()
from pakudex import Pakudex
print("Welcome to Pakudex: Tracker Extraordinaire!")
input_is_invalid = True
while input_is_invalid:
    #I do not know if they want us to check, but just in case.
    try:
        user_c = int(input("Enter max capacity of the Pakudex: "))
        if user_c >= 1:
            input_is_invalid = False
        else:
            print("Please enter a valid size.")
    except:
        print("Please enter a valid size.")
UserPakudex = Pakudex(user_c)
print(f"The Pakudex can hold {UserPakudex.get_capacity()} species of Pakuri.")
def menu_manager(userInput):
    if userInput == "1":
        #List Pakuri
        k = UserPakudex.get_species_array()
        if k == None:
            print("No Pakuri in Pakudex yet!")
        else:
            print("Pakuri In Pakudex:")
            for i,paku_species in enumerate(k):
                print(f"{i+1}. {paku_species}")
    if userInput == '2':
        #Show Pakuri
        selected_paku = str(input("Enter the name of the species to display: "))
        k = UserPakudex.get_stats(selected_paku)
        if k == None:
            print("Error: No such Pakuri!")
        else:
            print()
            print(f"Species: {selected_paku}")
            print(f"Attack: {k[0]}")
            print(f"Defense: {k[1]}")
            print(f"Speed: {k[2]}")
    if userInput == '3':
        #Add Pakuri
        if UserPakudex.get_size() < UserPakudex.get_capacity():
            selected_paku = str(input("Enter the name of the species to add: "))
            k = UserPakudex.add_pakuri(selected_paku)
            if k:
                print(f"Pakuri species {selected_paku} successfully added!")
            else:
                print(UserPakudex.current_error)
        else:
            print("Error: Pakudex is full!")
    if userInput == '4':
        #Evolve Pakuri
        selected_paku = str(input("Enter the name of the species to evolve: "))
        k = UserPakudex.evolve_species(selected_paku)
        if k:
            print(f"{selected_paku} has evolved!")
        else:
            print(UserPakudex.current_error)
    if userInput == '5':
        #Sort Pakuri
        print("Pakuri have been sorted!")
        UserPakudex.sort_pakuri()
    if userInput == '6':
        #Exit
        print("Thanks for using Pakudex! Bye!")
        exit()
valid = ['1', '2', '3', '4', '5', '6']
while True:
    print("""
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
""")
    user_input = input("What would you like to do? ")
    if user_input in valid:
        menu_manager(user_input)
    else:
        print("Unrecognized menu selection!")
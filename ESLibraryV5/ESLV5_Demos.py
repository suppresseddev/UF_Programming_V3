#This file will serve as an example to any curious programmers how to use ES Library.
import ESLV5 as esl

#Example TABIMC use:
bot = esl.TABIMC(name = "Demo Bot", title = "(Friend)", action_message = "is saying")
#When running:
bot.say("Hello World!")
#You will see:
#   (Friend) Demo Bot is reporting Hello World!
#You also have the option to have no title or action_message, but you have to deliberately put "" as the input.

#Example TSNM use:
our_menu = esl.TSNM_Menu("our_menu", width = 50)
our_menu.add_page("mainmenu", "Main Menu")
our_menu.get_page("mainmenu").set_description("This is where some magic may or may not happen, depending on if a feature "
                                              "like this is interesting to any parties.")
#You can leave page descriptions as one long string, they will be formatted when displayed.
our_menu.load_page("mainmenu")
#It will now display the menu I told it to!

#Now for something more complicated.
addition_page = esl.TSNM_Page(our_menu, "addpage", "Addition Test")
def addition_input_handler(x):
    try:
        int(x)
        return True
    except:
        print("You must use some kind of number for addition.")
        return False
#If you need to handle your parameter relative to eachother, you should consider using tuples or lists as individual inputs.
def addition(x,y):
    print(f"The sum of {x} and {y} is {int(x)+int(y)}!")
addition_page.set_function(addition)
addition_page.set_description("This page exists solely to test how my pages work, and see if they are just flashy or if they"
                              " provide meaningful structure.")
addition_page.add_input("number 1", input_handler = addition_input_handler)
addition_page.add_input("number 2", input_handler = addition_input_handler)
#There is another property called input_context, this displays a brief message when the user gives the input.

#This is an example of a TSNM input handler.
while True:
    our_menu.update()
    #Renders the selected page for the end user.

    #Everything below is how you would go about handling input for a generic "user picks the page" program.
    valid_pages = our_menu.pages.keys()
    print(f"Available Pages: ", end = "")
    for line in esl.create_paragraph(', '.join(valid_pages), 30, indent=False):
        print(line)
    input_invalid = True
    menu_input = ""
    while input_invalid:
        menu_input = input(f"Which page would you like to navigate to? ")
        if menu_input in valid_pages:
            input_invalid = False
        else:
            print("That's not a valid page.")

    our_menu.load_page(menu_input)

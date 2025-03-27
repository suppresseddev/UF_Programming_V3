import sys

#I don't understand the use for this file.
#It SEEMS to be intended to create the default cows, but I can do that myself, y'know? No foul?
import heifer_generator as hg

from cow import *

#Forcing students to do over-restricted programming to simulate OOP in Python, is crazy.

#Doing what heifer_generator.py does, but myself.
Heifer = Cow("heifer")
Heifer.set_image(0)
Kitteh = Cow("kitteh")
Kitteh.set_image(1)
#Differnt potential outputs are these next functions.
def list_cows():
    #This will probably use the cow() class, so ignore it for now.
    k = "Cows available: "
    k += ' '.join(Cow.All_Cows_Names)
    print(k)
def cow_message(msg, cow = None):
    #This will print the message from the cow. Yes this is stupid.
    if cow == None:
        print(msg)
        print(Cow.quote_lines + Cow.cow_images[0])
    else:
        print(msg)
        print(cow.image)
#Idk if main() is needed here.
# def main():
    #Our teachers are weird.
command = sys.argv
#Refers to the object.
cow = None
cow_i = -1
msgAfter = False
msgBefore = False
for i, arg in enumerate(command):
    #First check for any command.
    if arg == "-n":
        #If cow is named, commence the fetch protocol.
        #Just learned that they only want it to work like this if -n is the first argument.
        #My dynamic version is still good, BUT I can just restrict it with an if statement.
        if i == 1:
            if command[i + 1] in Cow.All_Cows_Names:
                cow = Cow.get_cow(command[i + 1])
            else:
                #Error Response
                print(f"Could not find {command[i + 1]} cow!")
                exit()
            if i == 1:
                msgAfter = True
            else:
                msgBefore = True
            #Index of the portion that is a command.
            cow_i = i
    if arg == "-l":
        #If chosen to list cows, do as follows.
        list_cows()
        exit()
#With context now known, construct the message.
msg = ""
if msgAfter:
    #Count indexes after the cow name.
    for t in range(cow_i + 2, len(command)):
        msg += command[t] + " "
elif msgBefore:
    #Count indexes before the cow name.
    for t in range(1, cow_i):
        msg += command[t] + " "
else:
    #Use all arguments as message inputs.
    for t in command[1:]:
        msg += t + " "
#The above process(es) are meant to make the command magic more dynamic because it is not restricted to a, b, c format.

#Now this SHOULD always run correctly.
if msg == "":
    exit()
else:
    cow_message(msg[:-1], cow = cow)
#Python Basics
#Variable Types
#Int
int = 10
#String
string = "Ten"
#Float
flt = 10.0
#Tuple
tup = (10, 10)
#Bool
buul = True

#Do something with em'
def stringstuff (a,b):
    if (a not in range(0, len(string))):
        print("")
    if (b not in range(0, len(string))):
        print("")
from random import *
def isEven(choice):
    choice = choice // 1  # You solved this part, that was neat.
    if choice%2 == 0:
        #print(str(choice)+" is an even number.")
        return(True)
    else:
        #print(str(choice)+" is an odd number.")
        return(False)
#Example
print("\nExcericse 1\n")
isEven(503)
isEven(412)
isEven(0)
isEven(4)
def count_four(choices):
    total = 0
    for item in choices:
        if item == 4 : total += 1
    print("The total count of '4' "+"is "+str(total)+".")
#example
print("\nExercise 2\n")
list1 = [10,4,4,2,42]
list2 = [4,4,5,5,4]
count_four(list1)
count_four(list2)
def complexfunction(choices, limita = 401, limitb = 1000):
    sum = 0
    errorcutoff = False
    limitbroke = False
    for item in choices:
        if not(limitbroke):
            if ((item < limita) and (isEven(item))):
                sum += item
                print(item)
                if sum > limitb:
                    print("Sum of {"+str(sum)+"} exceeds limit of {"+str(limitb)+"}")
                    limitbroke = True
        else:
            if ((item < limita) and (isEven(item))):
                errorcutoff = True
                break
    if sum == 0 : print("No items were less than {"+str(limita)+"} and even.")
    if errorcutoff : print("Not all items that were less than {"+str(limita)+"} and even were printed")
#generating a new list
list3 = [591, 606, 722, 412, 377, 487, 216, 957, 166, 457, 283, 818, 348, 475, 462, 175, 833, 844, 758, 833]
#for i in range(0,20):
#    list3.append(randint(0, 1000))
#exericse 3
print("\nExercise 3\n")
print(list3)
complexfunction(list3)



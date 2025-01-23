# Create 3 variables, assign numeric values and strings; display them on the screen with and without the print statement.
import string
global qnum
qnum = 1
def prinq():
    global qnum
    print(f"\nQuestion #{qnum}")
    qnum += 1
prinq()
mystring = "Python"
myint = 9
myfloat = 6.0
#printing without 'print'
mystring
myint
myfloat
#printing with 'print'
print(mystring)
print(myint)
print(myfloat)
prinq()
# What happens if you divide an integer with a decimal? Show your answer with an example.
print("It should become a float.")
print(myint/myfloat)
prinq()
# Print the first and last colors from the following list.
colorlist = ['Red','Green','White' ,'Black']
print(colorlist[0])
print(colorlist[len(colorlist)-1])
prinq()
# Insert “Blue” in 3rd position of above list.
colorlist.insert(2, "Blue")
prinq()
# Create a list with the first names of your family. What data type is best used for the names?
famlist = ["Robert", "Emily", "Emily", "Robert", "Elijah"]
prinq()
# Create a dictionary, with the names of your relatives as values and your relationship to them as keys; print out its content.
famdict = {
    "Sister" : "Emily",
    "Father" : "Robert",
    "Mother" : "Emily",
    "Brother" : "Robert"
}
print(famdict)
prinq()
# Write a program to display the value of "eyes" in the following dictionary:
dict1 = {'name': 'Lucas', 'eye color': 'brown', 'height': 6, 'weight': 160}
print("dict1['eyes'] does not exist")
print(dict1['eye color'])
prinq()
# Write a program to display the characters from the beginning to position 6 (excluded) in the following string:
qstring1 = "Introduction to Data Analytics"
print(qstring1[:6])
prinq()
# Write a program to display the characters from the second last in the above string.
print(qstring1[len(qstring1)-2])
prinq()
# Write a program to concatenate the following two lists:
L1 = [1,2,3,4]
L2 = ['a','b','c']
print(L1+L2)
prinq()
# Write a program to change the second item in L2 to 'q' and print the new list.
L2[1] = 'q'
print(L2)
prinq()
# Can lists have items with the same value? Show this with an example.
L3 = [0, 0, 0, 0, 3, 4, 5, 6]
print(L3)
print("Yes. Obviously.") #I'm joking
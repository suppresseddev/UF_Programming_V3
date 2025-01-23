qnum = 1
def question():
    global qnum
    print(f"\nQuestion Number {qnum}:\n")
    qnum += 1
import numpy as np
question()
# For the following matrix:
matrix = np.array([[12, 23, 45, 21],[45, 67, 34, 90],[11, 12, 13, 14],[54, 67, 78, 34]])
print(matrix)
question()
# a. get the second row
print(matrix[1,:])
question()
# b. get the third column
print(matrix[:,2])
question()
# c. get the element on the second row and third column.
print(matrix[1,2])
question()
# In the following example, write a numpy code to select elements placed at corners of the array and return it as a 2X2 matrix.
matrix2 = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
print(f"{matrix2}\n")
def corners(arr):
    topleftcorner = arr[0, 0]
    toprightcorner = arr[0, (len(arr[0])-1)]
    bottomleftcorner = arr[-1, 0]
    bottomrightcorner = arr[-1, (len(arr[-1])-1)]
    return(np.array([[topleftcorner, toprightcorner],[bottomleftcorner, bottomrightcorner]]))
print(corners(matrix2))
question()
# Replace all the odd numbers with -10 in the matrix provided in question 2.
matrix2_alt = matrix2.copy()
for axispos, axis in enumerate(matrix2):
    for itempos, item in enumerate(axis):
        if (item%2 != 0): matrix2_alt[axispos, itempos] = -10
print(matrix2_alt)
question()
# Get all the items between 4 to 10 in the matrix provided in question 2.
fourTOten = []
for axispos, axis in enumerate(matrix2):
    for itempos, item in enumerate(axis):
        if ((item < 10) and (item > 4)):
            fourTOten.append(int(item))
print(fourTOten)
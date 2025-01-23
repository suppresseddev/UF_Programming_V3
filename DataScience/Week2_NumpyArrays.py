# Excercise:
# 1. Write a NumPy program to create a 3x3 matrix with values of your choice.
# 2. Change the data types to float64.
# 3. Write a NumPy program to get the squred root of the elements.
# 4. Write a NumPy program to check if the elements (in original matrix) are greater than 10.
import numpy as np
qnum = 1
def question():
    global qnum
    print(f"\nQuestion Number {qnum}:\n")
    qnum += 1
question()
print("Creating an array.")
arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(f"This is the resultant array:\n{arr}")
question()
print("Changing the array type to 'float64'.")
arr = arr.astype('float64')
print(f"This is the resultant array:\n{arr}")
question()
print("Square-rooting the array.")
arrsqrt = arr**(1/2)
print(f"This is the resultant array:\n{arrsqrt}")
question()
print("Checking if each item in the array is greater than 10.")
arrbool = arr>10
print(f"This is the resultant array:\n{arrbool}")
print("Analyzing the results for each item in the array.")
for axispos, axis in enumerate(arrbool):
    # print(f"Axispos: {axispos}")
    # print(f"Axis: {axis}")
    for itempos, item in enumerate(axis):
        # print(f"itempos: {itempos}")
        # print(f"item: {item}")
        coords = (axispos, itempos)
        origitem = arr[(coords)]
        if item:
            print(f"The element at {coords} (Valued at {origitem}) is greater than 10.")
        else:
            print(f"The element at {coords} (Valued at {origitem}) is NOT greater than 10.")

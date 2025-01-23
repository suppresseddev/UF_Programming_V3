qnum = 1
def question():
    global qnum
    print(f"\nQuestion Number {qnum}:\n")
    qnum += 1
import numpy as np
question()
# 1. Create a 1D array with 9 elements and split it into 4 subarrays.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = np.array_split(arr, 4)
print(arr)
question()
# 2. Create two 2-D arrays and stack them as columns to make a single 2-D array. Show two different ways.
ar1 = np.array([1, 2, 3])
ar2 = np.array([4, 5, 6])
ar3 = np.column_stack((ar1, ar2))
print(ar3)
ar4 = np.vstack((ar1, ar2))
print(ar4)
question()
# 3. Create a 1D array and convert it to a 2D array with 2 rows.
ar1_3 = np.array([1, 2, 3, 4,])
ar1_3 = ar1_3.reshape((2,2))
print(ar1_3)
question()
# 4. Write a program to repeat elements of the array you created in previous question 4 times.
i = 1
while i < 5:
    print(f"Printing... {4-i} remaining")
    print(ar1_3)
    i += 1
question()
# 5. Create an array of shape 6 by 6 and split it into two arrays along the second axis.
arr_6 = np.array([[1],[2],[3],[4],[5],[6]])
arr_6 = np.vsplit(arr_6, 2)
print(arr_6)
question()
# 6. Swap rows and columns of the array you created in question 5.
arr_6 = np.swapaxes(arr_6, 0,1)
print(arr_6)
question()
# 7. For the following matrix, find the main diagonal and the diagnoals below and above the main diagonals.
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
d = np.diagonal(matrix)
db = np.diagonal(matrix, -1)
da = np.diagonal(matrix, 1)
print(d)
print(db)
print(da)
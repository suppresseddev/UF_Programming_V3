import numpy as np
qnum = 1
def question():
    global qnum
    print(f"\nQuestion Number {qnum}:\n")
    qnum += 1
question()
# Create a 8*8 array (you can use np.random.random method to create random values).
arr1 = np.random.randint(0,25,(8,8))
print(arr1)
question()
# a. Find the minimum and maximum values. Find the min and max values across rows and columns.
arr1_maxoverrow = np.max(arr1, axis=1)
arr1_maxovercol = np.max(arr1, axis=0)
print(f"Maximum values in the rows: {arr1_maxoverrow}\nMaximum values in the columns: {arr1_maxovercol}")
question()
# b. Find the indices of the min and max values.
print(f"Indexes of row maximums: {np.argmax(arr1, axis=1)}\nIndexes of column maximums: {np.argmax(arr1, axis=0)}")
print("Personally, I don't trust the results of these indexes, unless I'm failing to understand how those work.")
# c. Find the mean value. Find the mean values across rows and columns.
arr1_meanoverrow = np.mean(arr1, axis=0)
arr1_meanovercol = np.mean(arr1, axis=1)
print("")
# d. Normalize the values.

# e. Convert the data types to integer (int32)

# Create another 8*8 matrix. Check if the values are equal to the values of your matrix in question 1.

# a. Subtract the mean of each row of the matrix from each element in that row.

# Write a NumPy program to compute the 70th percentile for all elements in a given array along the second axis.

# Write a NumPy program to round array elements to three decimals.

# Write a NumPy program to create a random array with 1000 elements and compute the average, variance, standard deviation of the array elements.

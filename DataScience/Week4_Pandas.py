import pandas as pd
qnum = 1
def question():
    global qnum
    print(f"\nQuestion Number {qnum}:\n")
    qnum += 1
question()
# Create a data dictionary that contains the data in DataFrame below. Covert your dictionary to DataFrame.
df = {'Name': ['Paul', 'Kim', 'Dawn', 'Ana', 'Rose'], 'Age' : [54, 61, 33, 28, 43]}
df = pd.DataFrame(df)
print(df)
# print(df.iloc[1]['Name'])
question()
# For the above DataFrame, write a code that extracts the the minimum age.
youngest = 100
for age in df['Age']:
    if age < youngest:
        youngest = age
i = df[df['Age'] == youngest].index[0]
print(i)
print(f"The youngest age present is {youngest} and their name is {df['Name'][i]}")
question()
# Change the lable of the indices to a, b, ..., e.
df.index = ['a', 'b', 'c', 'd', 'e']
print(df)
question()
# Add another column named "Weight" to the above DataFrame. Assign values in range of 140 to 145.
df['Weight'] = range(140, 145)
print(df)
question()
# Write a Pandas program to get the first 3 rows of above DataFrame.
print(df[:3])
question()
# Select two columns Weight and Age from the above DataFrame.
print(df['Weight'],df['Age'])
question()
# Write a Pandas program to select the rows where the age is greater than 40.
rows1 = df[df['Age'] > 40]
print(rows1)
question()
# Write a Pandas program to select the rows where the age is between 20 and 40.
rows2 = df[(df['Age'] < 40) & (df['Age'] > 20)]
print(rows2)
question()
# Write a Pandas program to change the weight of Kim to 130.
df.loc['b', 'Weight'] = 130
print(df['Weight']['b'])
question()
# Write a Pandas program to calculate the average of weights in above DataFrame.
avgweights = df['Weight'].mean()
print(avgweights)
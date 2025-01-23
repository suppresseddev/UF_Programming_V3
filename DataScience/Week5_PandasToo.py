import pandas as pd
qnum = 1
def question():
    global qnum
    print(f"\nQuestion Number {qnum}:\n")
    qnum += 1

print("We are working with this data set:\n")
data = pd.read_csv("covid-data.csv")
pd.set_option("display.max_rows", 100)
print(data)
question()
# Write a Pandas program to get the values of location column.
#(hint: unique() method returns the unique values in a column.)
q1 = data['location'].unique()
print(f"The following are the unique locations in this dataset:\n{q1}")
question()
# How many locations have been recorded?
q2 = len(q1)
print(f"There have been {q2} location(s) recorded.")
question()
# Write a Pandas program to select the rows where location is 'US'.
print("There are 0 instances of 'US' in the location data set.\n"
      "Basic sense tells me you meant, 'United States', so that is what I used.\n")
q3 = data[data['location'] == 'United States']
print(q3)
question()
# Write a Pandas program to to return the total number of death in the US so far.
q4 = q3['total_deaths'].sum()
print(f"There was {q4} deaths in the United States so far.")
question()
# Write a Pandas program to get the record where we had the maximum number of new cases in the US.
q5 = q3['new_cases'].max()
print(f"There was at most {q5} new cases in a day within the United States.")
question()
# Write a Pandas program to get the country with the maximum number of death so far.
data6 = data.drop(data[data['location'] == 'World'].index)
q6 = data6['total_deaths'].max()
q6 = data.index[data['total_deaths'] == q6].tolist()
q6 = data.at[q6[0], 'location']
print(f"The country with the maximum number of deaths so far is {q6}.")
question()
# Convert the first character of each element in column "location" to lowercase.
data7 = data['location']
def justoneupper(s):
    snew = f"{s[0].lower()}{s[1:]}"
    return snew
data7 = data7.apply(justoneupper)
print(data7)
question()
# Normalize column 'total_deaths' for Germany .
data8 = data[data['location'] == 'Germany']
def normalizer(x):
    xnew = (x-(data8['total_deaths'].mean()))/(data8['total_deaths'].std())
    return xnew
data8 = data8['total_deaths'].apply(normalizer)
print(f"Standardized total deaths for Germany.\n{data8}")
question()
# Range all the values you obtained in previous question such that
# the minimum value of the total deaths is 0 and max is 1.
def proportioner(x):
    range = data8.max() - data8.min()
    xnew = abs(x - data8.min())/range
    return xnew
data9 = data8.apply(proportioner)
print(f"Proportionalized total deaths for Germany.\n{data9}")
question()
# Define a new column that lables the records based on the
# number of new cases per day per million.
# Use the following (drop the world and international records first):
# if x < 1,500; low if 1,500 =< x <= 3,000; medium if x > 3,000; high (x is new cases per day)
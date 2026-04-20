# Create a dataframe of 5 column and 4 rows using pandas library and print it.
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Teacher'],
    'Salary': [70000, 80000, 60000, 50000]
}
df = pd.DataFrame(data)
print(df)

# Filter the dataframe on basis of user input and print the filtered dataframe.
age_filter = int(input("Enter the age to filter the dataframe: "))
filtered_df = df[df['Age'] > age_filter]
print(filtered_df)

# Add a new column to the dataframe which is the square of the age column and print the updated dataframe.
df['Age_Squared'] = df['Age'] ** 2
print(df)

# filter the dataframe based on the column on users choice and print the filtered dataframe.
column_choice = input("Enter the column name to filter the dataframe (Name, Age, City, Occupation, Salary): ")
value_choice = input("Enter the value to filter the dataframe: ")
filtered_df = df[df[column_choice] == value_choice]
print(filtered_df)

# Sort the dataframe based on the column on users choice and print the sorted dataframe.
sort_column = input("Enter the column name to sort the dataframe (Name, Age, City, Occupation, Salary): ")
sorted_df = df.sort_values(by=sort_column)
print(sorted_df)
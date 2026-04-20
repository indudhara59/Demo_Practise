# create dataframe and give user a drop down to choose to sort by name or age using switch case statement
import pandas as pd
data = {'Name': ['John', 'Jane', 'Doe', 'Smith'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)
print("How would you like to sort the data?")
print("1. Sort by Name")
print("2. Sort by Age")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    sorted_df = df.sort_values(by='Name')
    print(sorted_df)
elif choice == 2:
    sorted_df = df.sort_values(by='Age')
    print(sorted_df)
else:
    print("Invalid choice. Please enter 1 or 2.")
    
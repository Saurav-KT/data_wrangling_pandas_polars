from pathlib import Path
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40]
s = pd.Series(data)
# s.index=['a1','b1','c1','d1']
# print(s)

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

# df = pd.DataFrame(data)
# print(df)


# Basic data operations reading data from CSV
file_path= Path("data")/"Forest_world.csv"
with file_path.open("r") as file:

    # Check if the first row is being read as data instead of header
    # csv_data = pd.read_csv(file, header=0)

    # if the CSV uses semicolons instead of commas
    csv_data = pd.read_csv(file,delimiter=';')
    # print(df.head())
    # print(df.tail())
    # print(df.describe())
    # print(df.info())
    csv_data.columns = csv_data.columns.str.strip()

    # Selecting a single column
    # print(csv_data.get('Region_ID'))

    # Selecting multiple columns
    # print(csv_data[['Region_ID', 'Plot_ID']])

    # Selecting rows by index (using iloc and loc)
    # print(csv_data.iloc[0])
    print(csv_data.loc[0])



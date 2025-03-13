# Pandas for Data Manipulation
# Pandas is a powerful library for working with data in Python. 
# It provides data structures and operations for efficiently manipulating and analyzing datasets.

# Install Pandas (before using it) via terminal: pip install pandas

# Import Pandas library
import pandas as pd

# Example 1: Data Cleaning - Handling Missing Values
# Create a sample DataFrame with missing values
# DataFrame is a 2-dimensional labeled data structure with rows and columns
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', None],
        'Age': [28, 24, 35, 32, 40],
        'Country': ['USA', 'UK', 'Australia', 'Germany', 'France']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Output:
# Original DataFrame:
#     Name  Age    Country
# 0   John   28        USA
# 1   Anna   24         UK
# 2  Peter   35  Australia
# 3  Linda   32    Germany
# 4   None   40     France

# Drop rows with missing values
# .dropna() conducts a drop operation on the DataFrame to remove rows with missing values e.g. None
df_clean = df.dropna()

print("\nDataFrame after dropping rows with missing values:")
print(df_clean)

# Output:
# DataFrame after dropping rows with missing values:
#     Name  Age    Country
# 0   John   28        USA
# 1   Anna   24         UK
# 2  Peter   35  Australia
# 3  Linda   32    Germany

# Example 2: Data Filtering - Selecting Rows
# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
        'Age': [28, 24, 35, 32, 40],
        'Country': ['USA', 'UK', 'Australia', 'Germany', 'France']}
df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

# Output:
# Original DataFrame:
#     Name  Age    Country
# 0   John   28        USA
# 1   Anna   24         UK
# 2  Peter   35  Australia
# 3  Linda   32    Germany
# 4    Tom   40     France

# Select rows where Age is greater than 30
df_filtered = df[df['Age'] > 30]

print("\nDataFrame after filtering rows where Age > 30:")
print(df_filtered)

# Output:
# DataFrame after filtering rows where Age > 30:
#     Name  Age    Country
# 2  Peter   35  Australia
# 3  Linda   32    Germany
# 4    Tom   40     France

# Example 3: Data Grouping - GroupBy and Aggregate
# GroupBy is used to group data based on a specified column or set of columns.
# Aggregate is used to perform operations on the grouped data, such as summing, counting, or averaging.
# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
        'Age': [28, 24, 35, 32, 40],
        'Country': ['USA', 'USA', 'Australia', 'Germany', 'France'],
        'Sales': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

# Output:
# Original DataFrame:
#     Name  Age    Country  Sales
# 0   John   28        USA    100
# 1   Anna   24        USA    200
# 2  Peter   35  Australia    300
# 3  Linda   32    Germany    400
# 4    Tom   40     France    500

# Group by Country and calculate sum of Sales
# df.groupby('Country'): Groups the DataFrame df by the values in the 'Country' column.
# ['Sales'].sum(): Selects the 'Sales' column and computes the sum for each country.
# .reset_index(): Converts the grouped result back into a DataFrame by resetting the index.
df_grouped = df.groupby('Country')['Sales'].sum().reset_index()

print("\nDataFrame after grouping by Country and summing Sales:")
print(df_grouped)

# Output:
# DataFrame after grouping by Country and summing Sales:
#      Country  Sales
# 0  Australia    300
# 1     France    500
# 2    Germany    400
# 3        USA    300

# Advanced Example: Data Merging - Merging Two DataFrames
# Create two sample DataFrames
data1 = {'CustomerID': [1, 2, 3, 4, 5],
         'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
         'Age': [28, 24, 35, 32, 40]}
df1 = pd.DataFrame(data1)

data2 = {'CustomerID': [1, 2, 3, 4, 5],
         'Country': ['USA', 'UK', 'Australia', 'Germany', 'France'],
         'Sales': [100, 200, 300, 400, 500]}
df2 = pd.DataFrame(data2)

print("\nOriginal DataFrames:")
print("df1:")
print(df1)
print("\ndf2:")
print(df2)

# Output:
# Original DataFrames:
# df1:
#    CustomerID   Name  Age
# 0           1   John   28
# 1           2   Anna   24
# 2           3  Peter   35
# 3           4  Linda   32
# 4           5    Tom   40

# df2:
#    CustomerID    Country  Sales
# 0           1        USA    100
# 1           2         UK    200
# 2           3  Australia    300
# 3           4    Germany    400
# 4           5     France    500

# Merge df1 and df2 on CustomerID
df_merged = pd.merge(df1, df2, on='CustomerID')

print("\nMerged DataFrame:")
print(df_merged)

# Output:
# Merged DataFrame:
#    CustomerID   Name  Age    Country  Sales
# 0           1   John   28        USA    100
# 1           2   Anna   24         UK    200
# 2           3  Peter   35  Australia    300
# 3           4  Linda   32    Germany    400
# 4           5    Tom   40     France    500
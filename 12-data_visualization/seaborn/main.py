# Data Visualization with Seaborn
# Seaborn is a popular library for creating data visualization in Python.
# The difference between Matplotlib and Seaborn is that Seaborn is built on top of Matplotlib
# Providing a higher-level interface for creating more complex visualizations.

# Install seaborn, pandas, numpy and matplotlib (before using it) via terminal: pip install seaborn pandas numpy matplotlib

# Import necessary libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example 1: Simple Bar Plot
print("Example 1: Simple Bar Plot")
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 20, 15, 30]}
df = pd.DataFrame(data)
sns.set()
sns.barplot(x='Category', y='Value', data=df)
plt.title("Simple Bar Plot")
plt.show(block=False)
plt.pause(2)
plt.close()

# Example 2: Grouped Bar Plot
print("Example 2: Grouped Bar Plot")
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Value': [10, 20, 15, 30, 25, 35]}
df = pd.DataFrame(data)
sns.set()
sns.barplot(x='Category', y='Value', hue='Subcategory', data=df)
plt.title("Grouped Bar Plot")
plt.show(block=False)
plt.pause(2)
plt.close()

# Example 3: Heatmap
print("Example 3: Heatmap")
data = np.random.rand(10, 12)
df = pd.DataFrame(data)
sns.set()
sns.heatmap(df, annot=True, cmap='coolwarm', square=True)
plt.title("Heatmap")
plt.show(block=False)
plt.pause(2)
plt.close()

# Example 4: Boxplot
print("Example 4: Boxplot")
data = {'Category': ['A', 'B', 'C', 'D'] * 10,
        'Value': np.random.rand(40)}
df = pd.DataFrame(data)
sns.set()
sns.boxplot(x='Category', y='Value', data=df)
plt.title("Boxplot")
plt.show(block=False)
plt.pause(2)
plt.close()

# Advanced Example: Pairplot
print("Advanced Example: Pairplot")
data = {'Feature1': np.random.rand(100),
        'Feature2': np.random.rand(100),
        'Feature3': np.random.rand(100)}
df = pd.DataFrame(data)
sns.set()
sns.pairplot(df)
plt.title("Pairplot")
plt.show()
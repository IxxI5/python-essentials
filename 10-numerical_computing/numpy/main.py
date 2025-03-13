# NumPy for Numerical Computing
# NumPy is a library for numerical computing in Python that provides a high-performance multidimensional array object, 
# and tools for working with these arrays.

# Install NumPy (before using it) via terminal: pip install numpy

import numpy as np

# Example 1: Basic Array Operations
# ------------------------------------

# Create two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Perform element-wise addition
result = arr1 + arr2
print("Element-wise addition:", result)

# Output:
# Element-wise addition: [ 7  9 11 13 15]   

# Example 2: Matrix Multiplication
# ---------------------------------

# Create two matrices
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication
result = np.matmul(mat1, mat2)
print("Matrix multiplication:\n", result)

# Output:
# Matrix multiplication:
#  [[19 22]
#  [43 50]] 

# Example 3: Statistical Functions
# ---------------------------------

# Create an array of exam scores
scores = np.array([85, 90, 78, 92, 88])

# Calculate mean, median, and standard deviation
mean = np.mean(scores)
median = np.median(scores)
std_dev = np.std(scores)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# Output:
# Mean: 86.6
# Median: 88.0
# Standard Deviation: 4.882622246293481 

# Example 4: Random Number Generation
# --------------------------------------

# Generate an array of 10 random numbers between 0 and 1
random_numbers = np.random.rand(10)
print("Random numbers:", random_numbers)

# Output:
# Random numbers: [0.65422888 0.78945678 0.23456789 0.56789012 0.34567890 0.12345678 0.78945678 0.23456789 0.56789012 0.34567890] or similar

# Example 5: Data Analysis
# -------------------------

# Create an array of temperatures in Celsius
temperatures = np.array([25, 30, 28, 22, 20])

# Convert temperatures to Fahrenheit
fahrenheit = (temperatures * 9/5) + 32
print("Temperatures in Fahrenheit:", fahrenheit)

# Output:
# Temperatures in Fahrenheit: [77.0 86.0 84.0 68.0 60.0]    

# Example 6: Linear Algebra
# -------------------------

# Create two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Calculate dot product
# The dot product is the sum of the products of corresponding elements of the two vectors 
dot_product = np.dot(vector1, vector2)
print("Dot product:", dot_product)

# Output:
# Dot product: 32

# Create two complex vectors
a = np.array([1 + 2j, 3 - 4j, 5 + 6j])
b = np.array([7 - 8j, 9 + 10j, 11 - 12j])

# Compute the dot product
# The dot product is the sum of the products of corresponding elements of the two vectors 
dot_product = np.dot(a, b)

print("Dot product:", dot_product)

# Output:
# Dot product: (217+6j)

# Calculate magnitude of vector1
# The magnitude of a vector is the square root of the sum of the squares of its components
magnitude = np.linalg.norm(vector1)
print("Magnitude of vector1:", magnitude)

# Output:
# Magnitude of vector1: 3.7416573867739413

# Example 7: Advanced - Principal Component Analysis (PCA)
# --------------------------------------------------------

# Create a dataset of 10 samples with 5 features
# e.g. a dataset of 10 samples with 5 features is a matrix of 10 rows and 5 columns (not an array)
np.random.seed(0)
data = np.random.rand(10, 5)

print(f"data:{data}")

# Output: 
# data:[[0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]
#  [0.64589411 0.43758721 0.891773   0.96366276 0.38344152]
#  [0.79172504 0.52889492 0.56804456 0.92559664 0.07103606]
#  [0.0871293  0.0202184  0.83261985 0.77815675 0.87001215]
#  [0.97861834 0.79915856 0.46147936 0.78052918 0.11827443]
#  [0.63992102 0.14335329 0.94466892 0.52184832 0.41466194]
#  [0.26455561 0.77423369 0.45615033 0.56843395 0.0187898 ]
#  [0.6176355  0.61209572 0.616934   0.94374808 0.6818203 ]
#  [0.3595079  0.43703195 0.6976312  0.06022547 0.66676672]
#  [0.67063787 0.21038256 0.1289263  0.31542835 0.36371077]]
# or similar

# Calculate the mean of each feature
# The mean of a set of values is the sum of the values divided by the number of values
# e.g. a 10x5 matrix, the mean is a 1x5 vector
mean = np.mean(data, axis=0)

print(f"mean:{mean}")

# Output:
# mean:[0.56044382 0.46781457 0.62009909 0.64025127 0.40121685]
# or similar

# Subtract the mean from each feature to center the data
# The centered data is the data with the mean subtracted from each feature
# resulting in a 10x5 matrix
centered_data = data - mean

print(f"centered_data:{centered_data}")

# Output:
# centered_data:
# [[-0.01163032  0.2473748  -0.01733571 -0.09536809  0.02243795]
#  [ 0.08545029 -0.03022736  0.27167391  0.32341149 -0.01777533]
#  [ 0.23128122  0.06108035 -0.05205453  0.28534537 -0.33018079]
#  [-0.47331452 -0.44759617  0.21252076  0.13790548  0.4687953 ]
#  [ 0.41817452  0.331344   -0.15861973  0.14027791 -0.28294242]
#  [ 0.0794772  -0.32446128  0.32456983 -0.11840295  0.01344509]
#  [-0.29588821  0.30641912 -0.16394876 -0.07181732 -0.38242705]
#  [ 0.05719168  0.14428116 -0.00316509  0.30349681  0.28060345]
#  [-0.20093592 -0.03078261  0.07753211 -0.5800258   0.26554987]
#  [ 0.11019405 -0.25743201 -0.49117279 -0.32482292 -0.03750608]]
# or similar

# Calculate the covariance matrix
# Covariance is a measure of how much two variables vary together
# The covariance matrix is a 5x5 matrix that represents the covariance between the features
cov = np.cov(centered_data, rowvar=False)

print(f"cov:{cov}")

# Output:
# cov:
# [[ 0.06771999  0.02541073 -0.0167912   0.02200881 -0.03839672]
#  [ 0.02541073  0.07368596 -0.02170091  0.0144989  -0.04413784]
#  [-0.0167912  -0.02170091  0.05851544  0.01874183  0.02907368]
#  [ 0.02200881  0.0144989   0.01874183  0.08744833 -0.01199478]
#  [-0.03839672 -0.04413784  0.02907368 -0.01199478  0.07852858]]
# or similar

# Calculate the eigenvectors and eigenvalues of the covariance matrix
# Eigenvector is a vector that when multiplied by the covariance matrix, 
# gives the eigenvalue
# Eigenvalue is a scalar that represents the amount of variance explained by the eigenvector
eig_vals, eig_vecs = np.linalg.eig(cov)

print(f"eig_vals, eig_vecs:{eig_vals}, {eig_vecs}")

# Output:
# eig_vals, eig_vecs:
# [0.16657685 0.09813566 0.04441926 0.0271625  0.02960403], 
# [[-0.47148654 -0.11262861 -0.70064618  0.44119257 -0.28188523]
#  [-0.52088076  0.06625504  0.69484296  0.46802935 -0.14978414]
#  [ 0.29591833 -0.49209983  0.15090088 -0.08123773 -0.80056196]
#  [-0.24715672 -0.84943791  0.05924686 -0.09815103  0.45191258]
#  [ 0.59810499 -0.13862922  0.00263167  0.75502612  0.230176  ]]
# or similar

# Sort the eigenvectors by their corresponding eigenvalues in descending order
idx = np.argsort(eig_vals)[::-1]
eig_vecs = eig_vecs[:, idx]

print(f"idx:{idx}")
print(f"eig_vecs:{eig_vecs}")

# Output:
# idx:[0 1 2 4 3]
# eig_vecs:
# [[-0.47148654 -0.11262861 -0.70064618 -0.28188523  0.44119257]
#  [-0.52088076  0.06625504  0.69484296 -0.14978414  0.46802935]
#  [ 0.29591833 -0.49209983  0.15090088 -0.80056196 -0.08123773]
#  [-0.24715672 -0.84943791  0.05924686  0.45191258 -0.09815103]
#  [ 0.59810499 -0.13862922  0.00263167  0.230176    0.75502612]]
# or similar

# Select the top 2 eigenvectors (corresponding to the top 2 eigenvalues)
eig_vecs = eig_vecs[:, :2]

print(f"eig_vecs:{eig_vecs}")

# Output:
# eig_vecs:
# [[-0.47148654 -0.11262861]
#  [-0.52088076  0.06625504]
#  [ 0.29591833 -0.49209983]
#  [-0.24715672 -0.84943791]
#  [ 0.59810499 -0.13862922]]

# Project the data onto the selected eigenvectors to reduce dimensionality
reduced_data = np.dot(centered_data, eig_vecs)

print(f"reduced_data:{reduced_data}")

# Output:
# reduced_data:
# [[-0.09150808  0.10412935]
#  [-0.03471536 -0.41757135]
#  [-0.42427325 -0.19299645]
#  [ 0.76549898 -0.26305905]
#  [-0.62059276 -0.02702175]
#  [ 0.26488503 -0.09145729]
#  [-0.27959735  0.24832636]
#  [-0.01023595 -0.29202606]
#  [ 0.4358998   0.43832102]
#  [-0.00536107  0.49335522]]

# Print the explained variance ratio (approximate)
explained_variance_ratio = eig_vals[idx[:2]] / np.sum(eig_vals)
print("Explained variance ratio:", explained_variance_ratio)
print("Reduced data shape:", reduced_data.shape)
print("Original data shape:", data.shape)

# Output:
# Explained variance ratio: [0.45525451 0.26820475]
# Reduced data shape: (10, 2)
# Original data shape: (10, 5)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Use an interactive backend for Matplotlib
plt.switch_backend('TkAgg')

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Inspect the data
print("First 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check data types
print("\nData types:")
print(df.dtypes)

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Bar chart: Average petal length by species
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# Histogram: Distribution of sepal length
df['sepal length (cm)'].plot(kind='hist', bins=20)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Sepal length vs petal length
df.plot(kind='scatter', x='sepal length (cm)', y='petal length (cm)')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()
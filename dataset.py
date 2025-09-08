# =====================================
# Assignment: Data Analysis with Pandas & Matplotlib
# =====================================

# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
try:
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Error: Dataset not found.")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Check structure of the dataset
print("Dataset Info:")
print(df.info(), "\n")

# Check for missing values
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# Clean dataset (Iris has no missing values, but we include this step)
df = df.dropna()

# Task 2: Basic Data Analysis
print("Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Group by species and calculate mean of numerical columns
print("Mean of numerical columns grouped by species:")
grouped_means = df.groupby("target").mean()
print(grouped_means, "\n")

# Replace target codes with species names for readability
df["species"] = df["target"].map(dict(enumerate(iris_data.target_names)))

# Task 3: Data Visualization

# 1. Line chart - cumulative petal length as an example of trend
df_sorted = df.sort_values("petal length (cm)").reset_index(drop=True)
plt.figure(figsize=(8,5))
plt.plot(df_sorted.index, df_sorted["petal length (cm)"].cumsum(), label="Cumulative Petal Length")
plt.title("Line Chart: Cumulative Petal Length")
plt.xlabel("Index (sorted by petal length)")
plt.ylabel("Cumulative Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal length
plt.figure(figsize=(8,5))
plt.hist(df["sepal length (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# Observations
print("Observations:")
print("- Sepal and petal lengths show clear separation across species.")
print("- Versicolor is intermediate between Setosa and Virginica in most measurements.")
print("- Histogram shows sepal length clusters roughly around 5-6 cm.")
print("- Scatter plot confirms Setosa species are clearly distinct (shorter petals and sepals).")


hasattr
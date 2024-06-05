import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('medical_cost.csv')

# Data Cleaning

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Handle missing values
# Fill missing values in numeric columns with the mean
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# For categorical columns, fill missing values with the mode
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Data Transformation

# Convert data types if necessary (example: ensuring 'Age' is an integer)
df['age'] = df['age'].astype(int)

# Create new calculated fields (example: calculating age group)
df['Age Group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 65, 100], labels=['0-18', '19-35', '36-50', '51-65', '66+'])

# Normalize/Standardize data (example: standardizing 'charges' column)
scaler = StandardScaler()
df['Charges Standardized'] = scaler.fit_transform(df[['charges']])

# Save the cleaned and transformed dataset
df.to_csv('cleaned_healthcare_dataset.csv', index=False)

print("Data preparation completed.")

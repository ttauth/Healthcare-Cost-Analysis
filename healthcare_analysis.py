import pandas as pd
import sqlite3
import numpy as np


conn = sqlite3.connect('healthcare_analysis.db')


total_expenditure = pd.read_sql_query('SELECT SUM(charges) AS total_expenditure FROM healthcare_data;', conn)
average_expenditure = pd.read_sql_query('SELECT AVG(charges) AS average_expenditure FROM healthcare_data;', conn)
expenditure_by_region = pd.read_sql_query('SELECT region, AVG(charges) AS average_expenditure FROM healthcare_data GROUP BY region;', conn)
expenditure_by_smoker = pd.read_sql_query('SELECT smoker, AVG(charges) AS average_expenditure FROM healthcare_data GROUP BY smoker;', conn)


print("Total Expenditure:", total_expenditure['total_expenditure'][0])
print("Average Expenditure:", average_expenditure['average_expenditure'][0])
print("Expenditure by Region:\n", expenditure_by_region)
print("Expenditure by Smoker Status:\n", expenditure_by_smoker)
data = pd.read_sql_query('SELECT age, bmi, children, charges FROM healthcare_data;', conn)


print("DataFrame Columns:", data.columns)


correlation_age_charges = np.corrcoef(data['age'], data['charges'])[0, 1]
correlation_bmi_charges = np.corrcoef(data['bmi'], data['charges'])[0, 1]
correlation_children_charges = np.corrcoef(data['children'], data['charges'])[0, 1]


print("Correlation between Age and Charges:", correlation_age_charges)
print("Correlation between BMI and Charges:", correlation_bmi_charges)
print("Correlation between Children and Charges:", correlation_children_charges)


conn.close()

-- healthcare_cost_analysis.sql

-- Create Table
CREATE TABLE IF NOT EXISTS healthcare_data (
    ID INTEGER PRIMARY KEY,
    Age INTEGER,
    Sex TEXT,
    BMI REAL,
    Children INTEGER,
    Smoker TEXT,
    Region TEXT,
    Charges REAL
);

-- Import Data (Assuming this is done through Python as shown previously)
-- .mode csv
-- .import medical_cost.csv healthcare_data

-- Sum of Charges
SELECT SUM(Charges) AS total_expenditure FROM healthcare_data;

-- Average Charges
SELECT AVG(Charges) AS average_expenditure FROM healthcare_data;

-- Average Charges by Region
SELECT Region, AVG(Charges) AS average_expenditure FROM healthcare_data GROUP BY Region;

-- Average Charges by Smoker Status
SELECT Smoker, AVG(Charges) AS average_expenditure FROM healthcare_data GROUP BY Smoker;

-- Extract necessary data for correlation calculations
SELECT Age, BMI, Children, Charges FROM healthcare_data;

import numpy as np #linear algebra
import pandas as pd #data processing
import matplotlib.pyplot as plt
import seaborn as sns
telecom=pd.read_csv('telecom.csv')
print(telecom.head())   
print(len( telecom),telecom.shape)
print ( type(telecom))
print(telecom.columns)
print(telecom.describe())
x=telecom['InternetService'].value_counts()
print(x)
Fiber=telecom[telecom['InternetService']=='Fiber optic']
print(Fiber.head())
print(len(Fiber))
DSL=telecom[telecom['InternetService']=='DSL']
print(DSL.head())
print(len(DSL))
sorted_telecom=telecom.sort_values(by=['MonthlyCharges','TotalCharges'],
ascending=[True, False]) 
print(sorted_telecom.head(10))
#Internet Service Type Distribution
plt.figure(figsize=(8,6))
sns.countplot(data=telecom,x='InternetService',palette='Set2')
plt.title('Nombre de clients par type de service Internet')
plt.xlabel('Type de service Internet')
plt.ylabel('Nombre de clients')
plt.show()
#Monthly charges distribution
plt.figure(figsize=(8,6))
sns.histplot(telecom['MonthlyCharges'],bins=30,kde=True,color='blue')
plt.title('Distribution des Monthly Charges')
plt.xlabel('Monthly Charges')
plt.ylabel('Nombre de clients')
plt.show()
#Boxplot MonthlyCharges vs InternetService
plt.figure(figsize=(8,5))
sns.boxplot(data=telecom, x='InternetService', y='MonthlyCharges', palette='Set3')
plt.title('Monthly Charges par type de service Internet')
plt.show()
# --- Relation tenure vs MonthlyCharges ---
plt.figure(figsize=(8,6))
sns.scatterplot(data=telecom, x='tenure', y='MonthlyCharges', hue='InternetService', alpha=0.6)
plt.title('Tenure vs Monthly Charges')
plt.xlabel('Tenure (mois)')
plt.ylabel('Monthly Charges')
plt.show()
#Top 10 clients with the highest charges
sorted_telecom = telecom.sort_values(by=['MonthlyCharges','TotalCharges'], ascending=[False, False])
print("Top 10 des clients les plus chers :")
print(sorted_telecom.head(10))
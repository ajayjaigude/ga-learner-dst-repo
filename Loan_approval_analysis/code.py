# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
#bank_data.head()
#bank_data.shape

categorical_var = bank_data.select_dtypes(include = 'object')
#print(categorical_var)
print(categorical_var.columns)

numerical_var = bank_data.select_dtypes(include = 'number')
#print(numerical_var)
print(numerical_var.columns)

categorical_var.shape
numerical_var.shape

banks = bank_data.drop(['Loan_ID'],axis=1)
banks.shape

banks.isnull().sum()
bank_mode = banks.mode().iloc[0]
print(bank_mode)

# Fill the missing values with 
banks.fillna(bank_mode, inplace=True)

# check again all the missing values filled.
print(banks.isnull().sum())

banks.isnull().sum().values.sum()

## Step 3
avg_loan_amount = pd.pivot_table(banks,values=['LoanAmount'] ,index=['Gender','Married','Self_Employed'], aggfunc=np.mean)

print(avg_loan_amount['LoanAmount'][1],2)

## Step 4
# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)

## Step 5 
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

## Step 6

loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.agg([np.mean])
print(mean_values)




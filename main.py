import numpy as np
import pandas as pd
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression

def values_in_dataset(df):
 for columns in df.columns:
        if df[columns].dtype == 'object':
            print(columns + ':', df[columns].unique() )
def main():
    clean_data = pd.read_csv('Data-Set/train.csv')
    values_in_dataset(clean_data)
    print(clean_data.head(10))
    print(clean_data.describe())
    print(clean_data.isna().sum())
    
    df = clean_data.drop(columns='Loan_ID', axis=1)
    loanID = clean_data['Loan_ID']

    ##------Fix Null Spaces for Loan Amount-----##
    df.dropna(subset='LoanAmount', inplace=True)

    ##------Fix Null Spaces for CoApplicantIncome-----##
    null_values_coapp = df[df['CoapplicantIncome'].isna()] #empty data frame means that co-applicant income has no null values
    #print(null_values_coapp)

     ##------Fix Null Spaces for Applicant Income-----##
    null_values_app = df[df['ApplicantIncome'].isna()] #empty data frame means that applicant income has no null values
    #print(null_values_app)

    ##------Fix Null Spaces for Self_Employed and replaces them with No-----##
    null_values_SE = df[df['Self_Employed'].isna()]
    df['Self_Employed'].fillna('No', inplace=True) #if null then assume person is not self-emplyoed and assume is employeed
    df['Self_Employed'].replace('Yes', 1, inplace=True)
    df['Self_Employed'].replace('No', 0, inplace=True)
    #print(df)

    ##------Replace Objects in Education with number-----##
    #print(df.dtypes) #this shows that there are no nan values in graduates
    df['Education'].replace('Graduate', 1, inplace=True)
    df['Education'].replace('Not Graduate', 0, inplace=True)
    print(df)
    print(df.dtypes)


     ##------Replace Null Values-----##
    df['Gender'].replace('Male', 1, inplace=True)
    df['Gender'].replace('Female', 0, inplace=True)
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)


    ##------Replace Null and changed strings to integers (1 -> married, 0 -> not married) Values-----##
    df['Married'].fillna('No', inplace=True )
    df['Married'].replace('Yes', 1, inplace=True)
    df['Married'].replace('No', 0, inplace=True)


    ##------Fix Dependent Columns-----##
    df['Dependents'].replace('0', 0, inplace=True)
    df['Dependents'].replace('1', 1, inplace=True)
    df['Dependents'].replace('2', 2, inplace=True)
    df['Dependents'].replace('3+', 3, inplace=True)
    df['Dependents'].fillna(df['Dependents'].mean(), inplace=True)



  ##------Loan Amount Columns-----##
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)

 ##------Credit History Columns-----##
    df['Credit_History'].fillna(0, inplace=True )

##----Loan Status ----- ## 
    df['Loan_Status'].replace('Y', 1, inplace=True)
    df['Loan_Status'].replace('N',0, inplace=True)

     
    property_area_coded = pd.get_dummies(df['Property_Area'])
    df['row_number'] = df.reset_index().index
    property_area_coded['row_number'] = property_area_coded.reset_index().index
    df = df.merge(property_area_coded, on="row_number")
    df.drop("Property_Area", inplace=True, axis=1)
    df.drop("row_number", inplace=True, axis=1)


    print()
    print(df.isna().sum())
    print(df)

main()
import numpy as np
import pandas as pd
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.impute import KNNImputer


def print_columns(df):
    for column in df.columns:
        print(column)

def print_unique_columns(df):
    for column in df.columns:
        if df[column].dtype == "object":
            print(column + ":", df[column].unique())


def clean_data(df):

    df.drop("Loan_ID", inplace=True, axis=1)

    property_area_coded = pd.get_dummies(df['Property_Area'])
    df['row_number'] = df.reset_index().index
    property_area_coded['row_number'] = property_area_coded.reset_index().index
    df = df.merge(property_area_coded, on="row_number")
    df.drop("Property_Area", inplace=True, axis=1)
    df.drop("row_nwumber", inplace=True, axis=1)

    df["Gender"].replace("Male", 0, inplace=True)
    df["Gender"].replace("Female", 1, inplace=True)
    df["Married"].replace("Yes", 1, inplace=True)
    df["Married"].replace("No", 0, inplace=True)
    df["Loan_Status"].replace("Y", 1, inplace=True)
    df["Loan_Status"].replace("N", 0, inplace=True)
    df["Education"].replace("Graduate", 1, inplace=True)
    df["Education"].replace("Not Graduate", 0, inplace=True)
    df["Self_Employed"].replace("No", 0, inplace=True)
    df["Self_Employed"].replace("Yes", 1, inplace=True)
    df["Dependents"].replace("0", 0, inplace=True)
    df["Dependents"].replace("1", 1, inplace=True)
    df["Dependents"].replace("2", 2, inplace=True)
    df["Dependents"].replace("3+", 3, inplace=True)

    #fill null values
    df["Gender"].fillna(df["Gender"].mode()[0], inplace=True)
    df["Married"].fillna(0, inplace=True)
    df["Dependents"].fillna(0, inplace=True)
    df["Self_Employed"].fillna(0, inplace=True)
    df.dropna(subset="LoanAmount", inplace=True)
    df["Credit_History"].fillna(0, inplace=True)
    df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].mode()[0], inplace=True)

    return df



def main():
    cleaned_data = clean_data(pd.read_csv('Data-Set/train.csv'))





def create_model(training_data, labels):
    log_regression = LogisticRegression()
    log_regression.fit(training_data, labels)
    print('no more data science lets create a game')

main()

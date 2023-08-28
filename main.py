import numpy as np
import pandas as pd
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression


def main():
    clean_data = pd.read_csv('Data-Set/train.csv')
    #print(clean_data)
    #print(clean_data.head())
    #print(clean_data.isna().sum())
    #print(clean_data.describe())
    #print(clean_data[clean_data.Credit_History ])
    print(clean_data["Credit_History"].value_counts())
    print(clean_data["Property_Area"].value_counts())


main()
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression

def clean_data():
    data_frame = pd.read_csv('Data-Set/cs-test.csv')

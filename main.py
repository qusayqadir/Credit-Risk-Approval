import numpy as np
import pandas as pd
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_decomposition import KFold
from sklearn.linear_model import LogisticRegression



def clean_data():
    data_frame = pd.read_csv('Data-Set/cs-test.csv')



clean_data
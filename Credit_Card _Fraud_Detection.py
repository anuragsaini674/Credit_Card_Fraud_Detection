#Importing Dependencies

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading Data
credit_card_data = pd.read_csv('F:\6th sem project\creditcard.csv')

credit_card_data.head()

import numpy as np
import pandas as pd


data = pd.read_csv('titanic.csv')


data.isna()
print(data['Age'].median())
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Age']

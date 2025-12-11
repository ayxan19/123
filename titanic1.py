import numpy as np
import pandas as pd

data = pd.read_csv('titanic.csv')
x = data.shape
print(x[0])
x2 = data['Age'].isnull().sum()
print(x2)
import numpy as np
import pandas as pd


data = pd.read_csv('titanic.csv')

x=len(data[(data['Sex'] == 'male')])
x2=len(data[(data['Pclass'] == 1)])
print(x)
print(x2)
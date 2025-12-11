import numpy as np
import pandas as pd
data = pd.read_csv('titanic.csv')
count = len(data[(data['Age'] < 18) & (data['Parch'] == 0)])
count1 = len(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)])
print(count1)
print(count)

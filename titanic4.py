import numpy as np
import pandas as pd
data = pd.read_csv('titanic.csv')
sum1 = data[data['Pclass'] == 1]['Fare'].sum()

kol = len(data[data['Pclass'] == 1])

srsum = sum1 / kol 

kol1=len(data[data['Pclass']==3])
vkol1=len(data[(data['Pclass']==3) & (data['Survived']==1)])
x3 = round(vkol1/kol1, 2)




print(round(srsum, 2))
print(x3)
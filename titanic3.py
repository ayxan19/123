import numpy as np
import pandas as pd
data = pd.read_csv('titanic.csv')
kol= data.shape

x=round(len(data[(data['Survived'] == 1)])/kol[0]*100, 2)
x2=len(data[(data['Pclass'] == 1)])

kol1=len(data[data['Sex']=='female'])
vkol1=len(data[(data['Sex']=='female') & (data['Survived']==1)])
x3 = round(vkol1/kol1*100, 2)

kol2=len(data[data['Sex']=='male'])
vkol2=len(data[(data['Sex']=='male') & (data['Survived']==1)])
x4 = round(vkol2/kol2*100, 2)

print(x)
print(x2)
print (x3)
print(x4)
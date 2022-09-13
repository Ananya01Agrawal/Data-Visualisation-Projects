# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 03:09:26 2022

@author: ADMIN
"""

#importing the library
import pandas as pd

import numpy as np

np.random.seed(10)

#reading the data
data=pd.read_csv('wc-at.csv')
print(data)

######################## First Business Moment Decision ##################################
#######################Measure of Central Tendency############################################

data['Waist'].mean()
data['AT'].mean()
data['Waist'].median()
data['Waist'].mode()
######################## Second Business Moment Decision ##################################
####################### Measure of Spread ############################################
data['Waist'].var()
data['Waist'].std()
data['Waist'].max()-data['Waist'].min()
data['Waist'].quantile([.25,.5,.75])

######################## Third Business Moment Decision ##################################
####################### Skewness  ########################################################

data['Waist'].skew()
import matplotlib.pyplot as plt
plt.hist(data['Waist'])

######################## Fourth Business Moment Decision ##################################
####################### Kurtosis  #######################################################

data['Waist'].kurt()

############################### Correlation ########################################
np.corrcoef(data.Waist,data.AT)
plt.scatter(y=data.Waist,x=data.AT,color='green')
